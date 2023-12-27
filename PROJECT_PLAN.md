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

## Dashboard Development Progress

### Completed Tasks:

- Created a new Python module `dashboard_utils.py` for backend interactions with Docker Swarm API and other services.
- Added placeholder functions `fetch_cluster_status` and `fetch_service_health` to simulate data fetching from services.
- Updated the `dashboard` view in `views.py` to include additional context data for the dashboard.
- Implemented initial JavaScript functions in `dashboard.js` for dynamic updates of the dashboard using AJAX.
- Started styling the dashboard with CSS in `dashboard.css` to match the project's "fantasy" theme.

### Pending Updates:

- Replace placeholder functions in `dashboard_utils.py` with actual Docker Swarm API interactions and service data retrieval.
- Enhance the `dashboard` view to handle AJAX requests efficiently and return structured JSON data.
- Refine JavaScript error handling in `dashboard.js` and ensure the dashboard components are updated correctly with new data.
- Complete the CSS styling in `dashboard.css` to fully realize the "fantasy" theme, focusing on responsiveness and design consistency.
- Test the frontend real-time updates to ensure accurate reflection of the cluster and service statuses.
- Implement necessary user authentication and authorization for dashboard access control.
- Conduct comprehensive testing of both backend and frontend to validate the dashboard's functionality and user experience.

## Codebase Verification and Corrections

### Completed Verifications:

- Ensured Django template tags are used correctly in `dashboard.html` for linking static files.
- Verified valid Python syntax and Django functionality in `views.py` and `dashboard_utils.py`.
- Confirmed correct URL pattern setup in `urls.py` for the dashboard view and data endpoint.
- Checked JavaScript functionality in `dashboard.js` for real-time updates and error handling.
- Reviewed CSS styling in `dashboard.css` for responsiveness and adherence to the "fantasy" theme.

### Corrections Made:

- Removed the Django template tag from the CSS file `dashboard.css` and provided a fallback background color. The background image URL will be set dynamically in the view or preprocessed to maintain separation of concerns and avoid mixing template logic with CSS.

### Next Steps:

- Update `dashboard_utils.py` with actual API interaction logic to fetch real-time data from Docker Swarm and other services.
- Implement error handling in the `dashboard_data` view to manage potential API request failures.
- Conduct thorough testing of the dashboard's real-time updates to ensure data accuracy and stability.
- Perform code reviews to maintain high standards of code quality and to facilitate knowledge sharing among team members.
- Document any challenges encountered during the implementation phase and the solutions applied to resolve them.

### Notes:

- Continuous integration and testing will be leveraged to catch issues early and ensure a smooth deployment process.
- Stakeholders will be kept informed of progress through regular updates to this project plan.
- Review and refactor the code to optimize performance, readability, and maintainability.
- As the development progresses, we will continue to document any challenges and solutions.
- Any changes to the project scope or timeline will be recorded to keep all stakeholders updated.
- Code reviews will be scheduled to ensure adherence to best practices and project standards.

## Hardware Utilization
## Progress Update

As of the latest update, the following progress has been made:

- The initial setup of the Django project within Docker containers has been completed.
- The Django settings have been configured to include the Home Assistant API URL and token.
- A new view has been added to the Django application to interact with the Home Assistant API and fetch its status.
- Environment variables related to the Django secret key and Home Assistant configuration have been added to the docker-compose.yml file.

Next steps include further development of the Django Dashboard, integration with other services, and the implementation of systems monitoring and push notifications. The user interface design will also be completed in line with the "fantasy" theme outlined in the project goals.

## Dashboard Development Progress

### Completed Tasks:

- Created a new Python module `dashboard_utils.py` for backend interactions with Docker Swarm API and other services.
- Added placeholder functions `fetch_cluster_status` and `fetch_service_health` to simulate data fetching from services.
- Updated the `dashboard` view in `views.py` to include additional context data for the dashboard.
- Implemented initial JavaScript functions in `dashboard.js` for dynamic updates of the dashboard using AJAX.
- Started styling the dashboard with CSS in `dashboard.css` to match the project's "fantasy" theme.

### Pending Updates:

- Replace placeholder functions in `dashboard_utils.py` with actual Docker Swarm API interactions and service data retrieval.
- Enhance the `dashboard` view to handle AJAX requests efficiently and return structured JSON data.
- Refine JavaScript error handling in `dashboard.js` and ensure the dashboard components are updated correctly with new data.
- Complete the CSS styling in `dashboard.css` to fully realize the "fantasy" theme, focusing on responsiveness and design consistency.
- Test the frontend real-time updates to ensure accurate reflection of the cluster and service statuses.
- Implement necessary user authentication and authorization for dashboard access control.
- Conduct comprehensive testing of both backend and frontend to validate the dashboard's functionality and user experience.

## Codebase Verification and Corrections

### Completed Verifications:

- Ensured Django template tags are used correctly in `dashboard.html` for linking static files.
- Verified valid Python syntax and Django functionality in `views.py` and `dashboard_utils.py`.
- Confirmed correct URL pattern setup in `urls.py` for the dashboard view and data endpoint.
- Checked JavaScript functionality in `dashboard.js` for real-time updates and error handling.
- Reviewed CSS styling in `dashboard.css` for responsiveness and adherence to the "fantasy" theme.

### Corrections Made:

- Removed the Django template tag from the CSS file `dashboard.css` and provided a fallback background color. The background image URL will be set dynamically in the view or preprocessed to maintain separation of concerns and avoid mixing template logic with CSS.

### Next Steps:

- Update `dashboard_utils.py` with actual API interaction logic to fetch real-time data from Docker Swarm and other services.
- Implement error handling in the `dashboard_data` view to manage potential API request failures.
- Conduct thorough testing of the dashboard's real-time updates to ensure data accuracy and stability.
- Perform code reviews to maintain high standards of code quality and to facilitate knowledge sharing among team members.
- Document any challenges encountered during the implementation phase and the solutions applied to resolve them.

### Notes:

- Continuous integration and testing will be leveraged to catch issues early and ensure a smooth deployment process.
- Stakeholders will be kept informed of progress through regular updates to this project plan.
- Review and refactor the code to optimize performance, readability, and maintainability.
- As the development progresses, we will continue to document any challenges and solutions.
- Any changes to the project scope or timeline will be recorded to keep all stakeholders updated.
- Code reviews will be scheduled to ensure adherence to best practices and project standards.

## Hardware Utilization


All of the hardware needs to will be utilized as much as possible. The Docker Swarm cluster will be configured to use all of the CPU, GPU, and RAM resources on the devices.