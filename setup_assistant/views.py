from django.shortcuts import render, redirect
from .forms import SetupForm
from django.conf import settings
import os

def setup_environment(request):
    if request.method == 'POST':
        form = SetupForm(request.POST)
        if form.is_valid():
            # Save the form data to environment variables or .env file
            config_data = form.cleaned_data
            with open('.env', 'w') as env_file:
                for key, value in config_data.items():
                    env_file.write(f'{key}={value}\n')
            # Update Django settings
            settings.configure(DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': config_data['db_name'],
                    'USER': config_data['db_user'],
                    'PASSWORD': config_data['db_pass'],
                    'HOST': config_data['db_host'],
                    'PORT': config_data['db_port'],
                }
            })
            # Redirect to a page that triggers the Docker stack deployment
            return redirect('deploy_stack')
    else:
        form = SetupForm()

    return render(request, 'setup_assistant/setup_form.html', {'form': form})
import subprocess

def deploy_stack(request):
    # Build the Docker images
    subprocess.run(['docker-compose', 'build'], check=True)
    # Deploy the Docker stack with PiHole
    subprocess.run(['docker', 'stack', 'deploy', '-c', 'compose/pihole.yml', 'homelab'], check=True)
    # Redirect to a success page or the dashboard
    return redirect('dashboard')