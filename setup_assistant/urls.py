from django.urls import path
from . import views

urlpatterns = [
    path('', views.setup_environment, name='setup_environment'),
path('deploy-stack/', views.deploy_stack, name='deploy_stack'),
]
