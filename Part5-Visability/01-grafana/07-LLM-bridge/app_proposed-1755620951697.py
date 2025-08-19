from fastapi import FastAPI, Query
import httpx
from numpy import mean, max as np_max, min as np_min
import os
import time
import json
import logging
import hashlib
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default values can be overite in `21-bridge-configmap.yaml`
PROM = os.getenv("PROM_URL", "http://prometheus-server:80")
CACHE_TTL = int(os.getenv("CACHE_TTL", "300"))  # 5 minutes default
MODEL_NAME = os.getenv("MODEL_NAME", "anthropic.claude-3-sonnet-20240229-v1:0")
BEDROCK_REGION = os.getenv("BEDROCK_REGION", "us-east-1")
BEDROCK_KEY = os.getenv("BEDROCK_KEY","")

api = FastAPI()
client = httpx.AsyncClient(timeout=60)
bedrock = boto3.client('bedrock-runtime', region_name=BEDROCK_REGION)

# Simple in-memory cache
cache = {}

def get_cache_key(query: str, minutes: int) -> str:
    return hashlib.md5(f"{query}:{minutes}".encode()).hexdigest()

def is_cache_valid(timestamp: float) -> bool:
    return time.time() - timestamp < CACHE_TTL

@api.get("/")
async def root():
    return {"message": "Metrics AI Bridge is running with AWS Bedrock"}

@api.get("/cache/stats")
async def cache_stats():
    valid_entries = sum(1 for entry in cache.values() if is_cache_valid(entry["timestamp"]))
    return {
        "total_entries": len(cache),
        "valid_entries": valid_entries,
        "cache_ttl": CACHE_TTL
    }

@api.post("/cache/clear")
async def clear_cache():
    cache.clear()
    return {"message": "Cache cleared"}

@api.get("/summary")
async def summarize(query: str = Query(...), minutes: int = 60):
    # Check cache first
    cache_key = get_cache_key(query, minutes)
    if cache_key in cache and is_cache_valid(cache[cache_key]["timestamp"]):
        logger.info(f"Cache hit for query: {query}")
        return cache[cache_key]["data"]
    # Get data from Prometheus
    now = int(time.time())
    start = now - minutes*60
    step = max(15, int(minutes*60/200))
    
    try:
        r = await client.get(f"{PROM}/api/v1/query_range", 
                           params={"query": query, "start": start, "end": now, "step": f"{step}s"})
        r.raise_for_status()
        response_data = r.json()
        data = response_data.get("data", {}).get("result", [])
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"Prometheus connection error: {e}")
        return {"summary": f"Error connecting to Prometheus: {str(e)}", "query": query}
    except json.JSONDecodeError as e:
        logger.error(f"Prometheus JSON decode error: {e}")
        return {"summary": "Invalid response from Prometheus", "query": query}

    # Calculate basic statistics
    series_stats = []
    for s in data:
        vals = [float(v[1]) for v in s["values"] if v[1] not in (None, 'NaN')]
        if not vals: continue
        series_stats.append({
            "metric": s.get("metric", {}),
            "avg": mean(vals),
            "max": np_max(vals),
            "min": np_min(vals),
            "last": vals[-1],
            "trend": vals[-1] - vals[0]
        })

    if not series_stats:
        return {"summary": "No data found for the selected time window", "query": query}

    # Send to AWS Bedrock
    prompt = f"""Analyze these metrics findings:
PromQL: {query}
Time window: {minutes} minutes
Statistics: {series_stats[:3]}

Provide a brief and practical summary."""

    try:
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {"role": "user", "content": f"You are a Senior SRE and DevOps metrics analyst. Be concise and practical. {prompt}"}
            ]
        })
        
        response = bedrock.invoke_model(
            modelId=MODEL_NAME,
            body=body
        )
        
        result = json.loads(response['body'].read())
        ai_summary = result['content'][0]['text']
                    
    except Exception as e:
        logger.error(f"{MODEL_NAME} connection error: {e}")
        ai_summary = f"Error connecting to {MODEL_NAME}: {str(e)}"


    result = {
        "summary": ai_summary,
        "query": query,
        "minutes": minutes,
        "stats_count": len(series_stats)
    }
    
    # Cache the result
    cache[cache_key] = {
        "data": result,
        "timestamp": time.time()
    }
    logger.info(f"Cached result for query: {query}")
    
    return result