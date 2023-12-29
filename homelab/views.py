from django.http import JsonResponse

import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .dashboard_utils import fetch_cluster_status, fetch_service_health

def pihole_status(request):
    # Placeholder for actual PiHole status fetching logic
    status = 'Active'  # This should be replaced with actual status check
    return JsonResponse({'status': status})

@login_required
def home(request):
    return HttpResponse("Hello, welcome to the homelab project!")

def dashboard(request):
    # Placeholder context data
    context = {
        'cluster_status': 'active',  # Example data, to be replaced with actual data fetching logic
        # Add more context data as needed
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def dashboard_data(request):
    data = {
        'cluster_status': fetch_cluster_status(),
        'service_health': fetch_service_health(),
        # Include additional data as needed
    }
    return JsonResponse(data)
from django.conf import settings
from django.http import JsonResponse

headers = {
    'Authorization': f'Bearer {settings.HOME_ASSISTANT_TOKEN}',
    'Content-Type': 'application/json',
}
response = requests.get(f"{settings.HOME_ASSISTANT_API_URL}states", headers=headers)
        response = requests.get(f"{settings.HOME_ASSISTANT_API_URL}states", headers=headers)
        response.raise_for_status()
        return JsonResponse(response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=502)

# Endpoint for fetching dashboard data in JSON format
def dashboard_data():
    data = {
        'cluster_status': fetch_cluster_status(),
        'service_health': fetch_service_health(),
        # Include additional data as needed
    }
    return JsonResponse(data)

fetch_home_assistant_states()
