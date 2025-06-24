#!/bin/bash
echo "Deploying scheduler and containers..."
docker build -t fisvdd -f docker/Dockerfile.fisvdd .
docker run --rm fisvdd
