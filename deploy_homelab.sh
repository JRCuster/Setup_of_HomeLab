#!/bin/bash

# Exit if any command fails
set -e

# Run setup script
echo "Running setup..."
./setup.sh

# Build the homelab_web image
echo "Building homelab_web image..."
docker build -t homelab_web:latest .

# Push the image to the Docker registry (if using a private registry, replace with your registry URL)
echo "Pushing homelab_web image to Docker registry..."
docker push homelab_web:latest

# Deploy the stack
echo "Deploying the Docker stack..."
docker stack deploy -c docker-compose.yml homelab

# Check the status of the stack deployment
echo "Checking the status of the stack deployment..."
docker stack services homelab

echo "Deployment script finished."