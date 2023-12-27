# User Manual

This document serves as a manual for users to understand how to use the HomeLab dashboard and services.

## Accessing the Dashboard
The dashboard can be accessed at `http://<master-node-ip>:8000/dashboard/`.

## Interacting with Services
Instructions on how to interact with Home Assistant, PostgreSQL, PiHole, Portainer Business Edition, and Systems Monitoring services.

### Accessing the Monitoring Tools
- **Prometheus**: Access Prometheus at `http://<master-node-ip>:9090/` to view metrics and monitoring data collected from the Docker Swarm cluster and services.
- **Grafana**: Access Grafana at `http://<master-node-ip>:3000/` to view dashboards that visualize the monitoring data. Default login credentials are admin/admin (please change these upon first login).

### Responding to Alerts
- When an alert is triggered, you will receive a notification through the configured notification channel (e.g., email, Slack).
- To respond to an alert, check the corresponding Grafana dashboard for detailed information about the metric that triggered the alert.
- Investigate the cause of the alert by examining the service or resource in question. Use the information provided by Prometheus and Grafana to guide your troubleshooting steps.

... (additional user instructions)