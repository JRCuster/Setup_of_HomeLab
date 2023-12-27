from django.urls import path
from . import views

urlpatterns = [
    path('', views.setup_environment, name='setup_environment'),
]
