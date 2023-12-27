from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the homelab project!")
import requests
from django.shortcuts import render

# New view for the dashboard
def dashboard(request):
    # Placeholder context data
    context = {
        'cluster_status': 'active',  # Example data, to be replaced with actual data fetching logic
        # Add more context data as needed
    }
    return render(request, 'dashboard.html', context)
from django.conf import settings
from django.http import JsonResponse

def home_assistant_status(request):
    try:
        headers = {
            'Authorization': f'Bearer {settings.HOME_ASSISTANT_TOKEN}',
            'Content-Type': 'application/json',
        }
        response = requests.get(f"{settings.HOME_ASSISTANT_API_URL}states", headers=headers)
        response.raise_for_status()
        return JsonResponse(response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=502)
