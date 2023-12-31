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
docker stack deploy -c <service-name>.yml <service-name>
```

This will start the service in the Docker Swarm cluster.

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
## PiHole Deployment
To deploy PiHole as a DNS and ad-blocking service, use the `compose/pihole.yml` Docker Compose file. Before deploying, ensure you customize the `compose/pihole.yml` file with your specific settings, such as timezone and admin password.

Run the following command to deploy PiHole to your Docker Swarm cluster:
```
docker stack deploy -c compose/pihole.yml pihole
```

After deployment, PiHole will be accessible on port 80 of the node where it is running. You can manage PiHole by accessing `http://<node-ip>/admin/` in a web browser, replacing `<node-ip>` with the IP address of the node running PiHole.

## Alerting and Notifications
Configure alerting rules in Prometheus to monitor the health of the Docker Swarm cluster and services. Set up Alertmanager to handle alerts and route them to the appropriate notification channels, such as email or Slack.

## SSL Configuration
Ensure that SSL is configured for secure communication. Follow the instructions in `security/ssl_config.conf` to set up SSL certificates and update the Nginx configuration to use HTTPS.

## Configuring ALLOWED_HOSTS

To allow your Django application to serve requests from different hosts, you need to update the `ALLOWED_HOSTS` setting in your `settings.py` file. Add the IP addresses or domain names that your application should serve. For example:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '10.60.1.91', '10.60.1.115']
```

## Correcting Syntax Errors in views.py

Ensure that all `return` statements in your `views.py` file are within function definitions. A `return` statement outside of a function will cause a `SyntaxError`. Here's an example of a correctly formatted view function:

```python
from django.shortcuts import render

def my_view(request):
    # Your view logic here
    return render(request, 'my_template.html', {'my': 'context'})
```
## Configuring ALLOWED_HOSTS

To allow your Django application to serve requests from different hosts, you need to update the `ALLOWED_HOSTS` setting in your `settings.py` file. Add the IP addresses or domain names that your application should serve. For example:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '10.60.1.91', '10.60.1.115']
```

## Correcting Syntax Errors in views.py

Ensure that all `return` statements in your `views.py` file are within function definitions. A `return` statement outside of a function will cause a `SyntaxError`. Here's an example of a correctly formatted view function:

```python
from django.shortcuts import render

def my_view(request):
    # Your view logic here
    return render(request, 'my_template.html', {'my': 'context'})
```
## Update ALLOWED_HOSTS in settings.py

To allow your Django application to serve requests from different hosts, update the `ALLOWED_HOSTS` setting in `settings.py`:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '10.60.1.91', '10.60.1.115']
```

Add any additional hostnames or IP addresses that your application should respond to.

## Template Configuration

Ensure that your views are pointing to the correct templates. For example, the `dashboard` view should render `dashboard/index.html`:

```python
# views.py

from django.shortcuts import render

def dashboard(request):
    # Your logic here
    return render(request, 'dashboard/index.html')  # Update this line to the correct template path
```

If you have a `dashboard.html` template that is not being used, consider removing it to avoid confusion.
## Final Steps
After completing the above steps, verify that all services are running correctly and that the dashboard is accessible and displaying data as expected. Consult the `USER_MANUAL.md` for guidance on using the dashboard and the monitoring tools.
... (additional setup instructions)