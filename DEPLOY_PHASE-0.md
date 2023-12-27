# Deployment Phase 0: Initial Build and Test

This document provides the initial steps to incrementally build and test the Docker setup for the HomeLab project, ensuring that each component is functioning correctly before proceeding to the next phase.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine
- Git installed on your machine

## Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/your-username/Setup_of_HomeLab.git
cd Setup_of_HomeLab
```

## Step 2: Build the Base Docker Image

Start by building a base Docker image that includes your Python environment and any system dependencies:

```bash
docker build -t homelab_base -f Dockerfile.base .
```

This Dockerfile should not include the application itself or any application-specific dependencies.

## Step 3: Test the Base Image

Run a container from the base image to ensure that it has been set up correctly:

```bash
docker run --rm -it homelab_base /bin/bash
```

You should be able to start a bash session within the container without encountering any errors.

## Step 4: Add Django Application to the Image

Once the base image is verified, extend it by copying your Django application and installing application-specific Python dependencies:

```Dockerfile
# Use the base image
FROM homelab_base

# Set the working directory to /app
WORKDIR /app

# Copy the Django project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
```

Build the updated image with the Django application:

```bash
docker build -t homelab_web .
```

## Step 5: Run Django Management Commands

With the Django application now part of the image, test running management commands to verify the setup:

```bash
docker run --rm homelab_web python manage.py check
```

This command should execute without any errors, indicating that Django is configured correctly.

## Step 6: Collect Static Files

Ensure that the `collectstatic` command is part of your `entrypoint.sh` script or Dockerfile, then rebuild the image and run the container to test static file collection:

```bash
docker build -t homelab_web .
docker run --rm homelab_web python manage.py collectstatic --noinput
```

Address any issues that arise during this step.

## Step 7: Launch the Application

If the `collectstatic` command completes successfully, you can proceed to launch the Django application using `docker-compose`:

```bash
docker-compose up --build
```

## Step 8: Verify the Application is Running

Check that the application is accessible and functioning by navigating to `http://localhost:8000/` in your web browser.

## Step 9: Review Logs and Troubleshoot

If you encounter any problems, use the logs to help diagnose and resolve issues:

```bash
docker-compose logs
```

## Conclusion

Following these steps will help you validate the Docker environment and ensure that the application is ready for further deployment phases. Once you have confirmed that everything is working as expected, you can proceed to `DEPLOY_PHASE-1.md` for the next steps in the deployment process.