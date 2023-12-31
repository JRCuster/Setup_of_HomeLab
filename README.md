
# Setup_of_HomeLab

## Project Overview

Setup_of_HomeLab is a Django-based project configured to run within Docker containers, leveraging Gunicorn as the WSGI server and Nginx as the web server with a PostgreSQL database backend.

## Prerequisites

- Docker
Please follow the instructions in `PRE_SETUP.md` before proceeding with the main setup.
- Docker Compose
- Git (for version control)

## Local Development Setup

Clone the repository to your local machine:

'''bash
git clone https://github.com/JRCuster/Setup_of_HomeLab.git
cd Setup_of_HomeLab
'''

Build and run the containers:

'''bash
Copy code
docker-compose up -d --build
'''

Access the application at http://localhost:8000/.
## Docker Swarm Setup

To initialize the Docker Swarm cluster on the master node, run:

```bash
./scripts/docker_swarm_init.sh
```

Follow the instructions output by the script to join worker nodes to the swarm.

Once the swarm is initialized, deploy the services using the provided Docker Compose files:

```bash
docker stack deploy -c docker-compose.yml homelab
```

For each additional service, use the respective Docker Compose file:

```bash
docker stack deploy -c compose/home_assistant.yml home_assistant
docker stack deploy -c compose/postgresql.yml postgresql
# Repeat for other services...
```

Ensure that all services are running correctly using:

```bash
docker service ls
```

## Configuration
The project is set up with Docker and includes:
- Dockerfile: Configuration for building the Django/Gunicorn application Docker image.
- docker-compose.yml: Docker Compose configuration for orchestrating multi-container Docker applications.
- requirements.txt: List of Python dependencies for the Django application.
- config/nginx: Nginx configuration files for serving the application.

To apply database migrations, run:

'''bash
Copy code
docker-compose exec web python manage.py migrate
'''

Create a Superuser
To create a superuser, run:

'''bash
Copy code
docker-compose exec web python manage.py createsuperuser
'''

Collect Static Files
To collect static files, run:

'''bash
Copy code
docker-compose exec web python manage.py collectstatic
'''

Environment Variables

Configure the environment variables as needed in docker-compose.yml and the Django settings.py file.
# Environment Variables
The following environment variables should be set:
- `DJANGO_SECRET_KEY`: The secret key used in production.
- `HOME_ASSISTANT_API_URL`: The API URL for Home Assistant.
- `HOME_ASSISTANT_TOKEN`: The long-lived access token for Home Assistant.


Contributing Instructions for how to contribute, report issues, and request features.

License
MIT License (MIT) © 2003 Custer

Contact drrohinshadow@gmail.com
