from django.urls import path
from .views import pihole_status

urlpatterns = [
    path('dashboard/pihole-status/', pihole_status, name='pihole_status'),
    # ... other url patterns ...
]
"""
URL configuration for homelab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Enable built-in auth views
    path('', include('your_app.urls')),  # Replace 'your_app' with your actual app name
]
"""
from django.contrib import admin
from django.urls import path
from . import views  # Make sure views is also correctly defined

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('home-assistant/status/', views.home_assistant_status, name='home-assistant-status'),
    path('dashboard/data/', views.dashboard_data, name='dashboard-data'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
