from django.urls import path
from django.contrib import admin
from homelab.views import pihole_status, dashboard

# Rest of the code...

urlpatterns = [
    path('', dashboard, name='home'),
    path('admin/', admin.site.urls),
    path('pihole-status/', pihole_status, name='pihole_status'),
    path('dashboard/', dashboard, name='dashboard'),
]
