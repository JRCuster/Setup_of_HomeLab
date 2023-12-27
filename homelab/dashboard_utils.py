import requests
from django.conf import settings

def fetch_cluster_status():
    # Actual API call to Docker Swarm API to fetch cluster status
    try:
        response = requests.get(f"{settings.DOCKER_SWARM_API_URL}/cluster_status")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}

def fetch_service_health():
    # Actual API call to fetch health status of services
    try:
        response = requests.get(f"{settings.SERVICE_API_URL}/service_health")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}