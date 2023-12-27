# Deployment Phase 1: Testing in Development Environment

This document outlines the steps to test the Docker Compose files and the Django application in a development environment.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine
- Git installed on your machine

## Step 1: Clone the Repository

Clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/Setup_of_HomeLab.git
cd Setup_of_HomeLab
```

## Step 2: Build Docker Images

Build the Docker images for all services defined in the Docker Compose file:

```bash
docker-compose build
```

## Step 3: Initialize Docker Swarm

Initialize Docker Swarm mode on your machine:

```bash
docker swarm init
```

## Step 4: Deploy Services Using Docker Compose

Deploy the services using the Docker Compose file:

```bash
docker stack deploy -c docker-compose.yml homelab
```

## Step 5: Verify Services Are Running

Check if the services are running correctly:

```bash
docker service ls
```

## Step 6: Test Django Application

Run the Django application container:

```bash
docker-compose up -d web
```

## Step 7: Apply Database Migrations

Apply the database migrations for the Django application:

```bash
docker-compose exec web python manage.py migrate
```

## Step 8: Collect Static Files

Collect the static files for the Django application:

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

## Step 9: Access the Django Application

Access the Django application by navigating to `http://localhost:8000/` in your web browser.

## Step 10: Review Application Logs

If you encounter any issues, review the application logs:

```bash
docker-compose logs web
```

## Conclusion

After completing these steps, you should have a running instance of the Django application and all related services in a Docker Swarm environment. This concludes Phase 1 of the deployment process. Ensure that all services are functioning as expected before proceeding to the next phase.
