# Project Plan Overview

## Project Name
Setup of HomeLab

## Project Goals
- Use Docker cluster to Setup AnythingLLM and Ollama to start working on the Project Management tasks.
- Setup a Docker Swarm cluster on 4 Raspberry Pi 4B devices.
- Deploy the following services to the Docker Swarm cluster:
  - Home Assistant
  - PostgreSQL
  - PiHole
  - Portainer Business Edition
  - Systems Monitoring
- Develop a Django Dashboard that provides a real-time view of the Docker Swarm cluster, including the status of pods, nodes, and services.
- Integrate the dashboard with Home Assistant, PostgreSQL, PiHole, Portainer Business Edition, and Systems Monitoring.
- Implement systems monitoring with push notifications to an app on the user's phone for maintenance tasks or emergencies.
- Design the dashboard with a "fantasy" theme, using images, fonts, and colors to create a visually appealing and engaging experience.

## Project Deliverables
- Docker Swarm cluster on 4 Raspberry Pi 4B devices
- Deployed Home Assistant, PostgreSQL, PiHole, Portainer Business Edition, and Systems Monitoring services
- Django Dashboard source code
- Documentation for the dashboard
- User training materials

## Project Milestones
- Milestone 1: Setup Docker Swarm cluster on Raspberry Pi 4B devices
- Milestone 2: Deploy Home Assistant, PostgreSQL, PiHole, Portainer Business Edition, and Systems Monitoring services to Docker Swarm cluster
- Milestone 3: Develop basic dashboard functionality
- Milestone 4: Integrate dashboard with Home Assistant, PostgreSQL, PiHole, Portainer Business Edition, and Systems Monitoring
- Milestone 5: Implement systems monitoring and push notifications
- Milestone 6: Complete user interface design
- Milestone 7: Complete project and deliver deliverables

## Subprojects
1. Docker Swarm Cluster Setup
2. Home Assistant Deployment
3. PostgreSQL Deployment
4. PiHole Deployment
5. Portainer Business Edition Deployment
6. Systems Monitoring Deployment
7. Django Dashboard Development

## Project Management Dashboard
A Google Sheets project management dashboard will be created to track the progress of the project. The dashboard will be automatically updated with the progress of each subproject. The dashboard will also include a separate tab for each subproject, with detailed information about the subproject. All of the data in the dashboard will be snapshotted to a database every hour.

## Progress Update

As of the latest update, the following progress has been made:

- The initial setup of the Django project within Docker containers has been completed.
- The Django settings have been configured to include the Home Assistant API URL and token.
- A new view has been added to the Django application to interact with the Home Assistant API and fetch its status.
- Environment variables related to the Django secret key and Home Assistant configuration have been added to the docker-compose.yml file.

Next steps include further development of the Django Dashboard, integration with other services, and the implementation of systems monitoring and push notifications. The user interface design will also be completed in line with the "fantasy" theme outlined in the project goals.
## Hardware Utilization
All of the hardware needs to will be utilized as much as possible. The Docker Swarm cluster will be configured to use all of the CPU, GPU, and RAM resources on the devices.