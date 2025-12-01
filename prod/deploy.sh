#!/bin/bash

set -e

echo "Logging into GitHub Container Registry (GHCR)..."
echo "$GHCR_TOKEN" | docker login ghcr.io -u angie-ng --password-stdin

cd ~/Deployment

# Pull the newly created and tested image from GHCR
echo "Pulling image ghcr.io/angie-ng/first-devops-project/dafnefirstapp:$IMAGE_TAG..."
docker compose pull

# Start services
echo "Applying compose..."
docker compose up -d

echo "Deployment completed!"

