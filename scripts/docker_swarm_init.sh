#!/bin/bash
# Initialize Docker Swarm on the master node
docker swarm init

# Output the join command for worker nodes
echo "To add a worker to this swarm, run the following command on the worker node:"
docker swarm join-token worker | grep "docker swarm join"