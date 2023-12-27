# Setup Guide

This document provides instructions for setting up the HomeLab project.

## Docker Swarm Initialization
To initialize the Docker Swarm cluster, execute the `scripts/docker_swarm_init.sh` script on the master node. This will set up the master node as the manager of the Docker Swarm cluster.

For worker nodes, use the join command provided at the end of the initialization output from the master node. It will look something like this:
```
docker swarm join --token SWMTKN-1-<token> <master-node-ip>:2377
```
Replace `<token>` and `<master-node-ip>` with the actual token and IP address.

## Service Deployment
Deploy the services using the Docker Compose files located in the `compose/` directory. For each service, navigate to its respective directory and run:
```
docker-compose up -d
```
This will start the service in detached mode.

## Dashboard Configuration
The Django Dashboard can be configured by setting the necessary environment variables in the `docker-compose.yml` file for the `web` service. Ensure that the `DATABASES` setting in `homelab/settings.py` is configured to connect to the PostgreSQL service.

After configuring the environment variables and database settings, you can access the dashboard at `http://<master-node-ip>:8000/dashboard/`.

## Monitoring Tools Setup
For setting up Prometheus and Grafana, use the `compose/monitoring.yml` Docker Compose file. Run the following command to start the monitoring services:
```
docker-compose -f compose/monitoring.yml up -d
```
Access Prometheus at `http://<master-node-ip>:9090/` and Grafana at `http://<master-node-ip>:3000/`. Configure Grafana to use Prometheus as the data source and set up the desired dashboards for monitoring.
Access Prometheus at `http://<master-node-ip>:9090/` and Grafana at `http://<master-node-ip>:3000/`. Configure Grafana to use Prometheus as the data source and set up the desired dashboards for monitoring.

... (additional setup instructions)