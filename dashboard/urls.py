from django.urls import path
from . import views

urlpatterns = [
path('setup/', views.setup_dashboard, name='setup_dashboard'),
    path('', views.index, name='index'),
]
