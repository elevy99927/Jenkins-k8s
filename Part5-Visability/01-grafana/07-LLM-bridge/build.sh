#!/bin/bash
docker buildx build --platform linux/amd64 -t elevy99927/metrics-ai-bridge:0.0.14 .
docker push elevy99927/metrics-ai-bridge:0.0.14
