#!/bin/bash
# Initialize Docker Swarm on the master node
docker swarm init

# Join worker nodes to the cluster (replace with actual tokens and IP addresses)
# docker swarm join --token <SWMTKN> <MASTER_NODE_IP>:2377