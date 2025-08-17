from fastapi import FastAPI, Query
import httpx
from numpy import mean, max as np_max, min as np_min
import os
import time
import json
import logging
import hashlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default values can be overite in `21-bridge-configmap.yaml`
PROM = os.getenv("PROM_URL", "http://prometheus-server:80")
OLLAMA = os.getenv("OLLAMA_URL", "http://phi3mini:11434")
CACHE_TTL = int(os.getenv("CACHE_TTL", "300"))  # 5 minutes default
MODEL_NAME = os.getenv("MODEL_NAME", "gemma:2b")

api = FastAPI()
client = httpx.AsyncClient(timeout=60)

# Simple in-memory cache
cache = {}

# Mock insights database
mock_insights = [
    {
        "id": "cpu_high_1",
        "query_pattern": "cpu.*usage.*high|cpu.*>.*80",
        "insight": "High CPU usage usually indicates memory leaks or infinite loops in application code",
        "action": "Check application logs and restart affected pods",
        "tags": ["cpu", "performance", "troubleshooting"],
        "confidence": 0.9
    },
    {
        "id": "memory_leak_1", 
        "query_pattern": "memory.*usage.*>.*90|container_memory.*high",
        "insight": "Memory usage above 90% often leads to OOM kills and service instability",
        "action": "Scale up memory limits or investigate memory leaks in application",
        "tags": ["memory", "oom", "scaling"],
        "confidence": 0.85
    },
    {
        "id": "disk_full_1",
        "query_pattern": "disk.*usage.*>.*85|filesystem.*full",
        "insight": "Disk usage above 85% can cause write failures and application crashes",
        "action": "Clean up logs, increase disk size, or implement log rotation",
        "tags": ["disk", "storage", "cleanup"],
        "confidence": 0.95
    }
]

def get_cache_key(query: str, minutes: int) -> str:
    return hashlib.md5(f"{query}:{minutes}".encode()).hexdigest()

def is_cache_valid(timestamp: float) -> bool:
    return time.time() - timestamp < CACHE_TTL

def search_insights(query: str) -> list:
    """Search for relevant insights based on query pattern"""
    import re
    relevant_insights = []
    
    for insight in mock_insights:
        pattern = insight["query_pattern"]
        if re.search(pattern, query, re.IGNORECASE):
            relevant_insights.append(insight)
    
    return relevant_insights

@api.get("/")
async def root():
    return {"message": "Metrics AI Bridge with Insights is running"}

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

@api.get("/insights")
async def get_insights():
    """Get all available insights"""
    return {
        "insights": mock_insights,
        "total": len(mock_insights)
    }

@api.get("/insights/search")
async def search_insights_endpoint(q: str = Query(...)):
    """Search for insights by query pattern"""
    relevant = search_insights(q)
    return {
        "query": q,
        "insights": relevant,
        "count": len(relevant)
    }

@api.post("/insights/add")
async def add_insight(insight: dict):
    """Add new insight (mock - in real implementation would save to database)"""
    new_insight = {
        "id": f"custom_{len(mock_insights) + 1}",
        "query_pattern": insight.get("query_pattern", ""),
        "insight": insight.get("insight", ""),
        "action": insight.get("action", ""),
        "tags": insight.get("tags", []),
        "confidence": insight.get("confidence", 0.5)
    }
    mock_insights.append(new_insight)
    logger.info(f"Added new insight: {new_insight['id']}")
    return {"message": "Insight added", "insight": new_insight}

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

    # Search for relevant insights
    relevant_insights = search_insights(query)
    insights_context = ""
    if relevant_insights:
        insights_context = "\n\nRelevant insights from past experience:\n"
        for insight in relevant_insights[:2]:  # Limit to top 2 insights
            insights_context += f"- {insight['insight']}\n- Recommended action: {insight['action']}\n"

    # Send to AI model via Ollama
    prompt = f"""Analyze these metrics findings:
PromQL: {query}
Time window: {minutes} minutes
Statistics: {series_stats[:3]}
{insights_context}

Provide a brief and practical summary considering the insights above."""

    try:
        ollama_response = await client.post(f"{OLLAMA}/api/chat", 
                                          json={
                                              "model": MODEL_NAME,
                                              "stream": False,
                                              "messages": [
                                                  {"role": "system", "content": "You are a DevOps metrics analyst. Be concise and practical. Use provided insights to enhance your analysis."},
                                                  {"role": "user", "content": prompt}
                                              ]
                                          })
        ollama_response.raise_for_status()
        logger.info(f"AI model response status: {ollama_response.status_code}")
        result = ollama_response.json()
        ai_summary = result.get("message", {}).get("content", "No response received from model")
                    
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"AI model connection error: {e}")
        ai_summary = f"Error connecting to AI model: {str(e)}"
    except json.JSONDecodeError as e:
        logger.error(f"AI model JSON decode error: {e}")
        ai_summary = "Invalid response from AI model"

    result = {
        "summary": ai_summary,
        "query": query,
        "minutes": minutes,
        "stats_count": len(series_stats),
        "insights_used": len(relevant_insights)
    }
    
    # Cache the result
    cache[cache_key] = {
        "data": result,
        "timestamp": time.time()
    }
    logger.info(f"Cached result for query: {query}")
    
    return result