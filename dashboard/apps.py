from django.apps import AppConfig
from django.db.models import BigAutoField
class DashboardConfig(AppConfig):
    default_auto_field = BigAutoField()
    name = 'dashboard'