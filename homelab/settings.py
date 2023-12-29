"""
Django settings for homelab project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os  # Added import statement for the 'os' module

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hc%4=(rovnz6&-&jfemw6y(ss&2o1f8ao-#eh&i+s2s%8s!#tt'
SECRET_KEY = (
    'django-insecure-hc%4=(rovnz6&-&jfemw6y(ss&2o1f8ao-#eh&i+s2s%8s!#tt'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

# Adjusted line length for ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '10.60.1.91', '10.60.1.115']

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ... other installed apps ...
    'dashboard.apps.DashboardConfig',  # Ensure this is the correct path to the dashboard app
    # ... other installed apps ...
]
# 'dashboard.apps.DashboardConfig',  # Uncomment or correct the path if the dashboard app exists

ROOT_URLCONF = 'homelab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'homelab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Home Assistant Configuration
HOME_ASSISTANT_API_URL = 'http://home_assistant:8123/api/'
HOME_ASSISTANT_TOKEN = 'your_long_lived_access_token'

# Docker Swarm API URL and token
DOCKER_SWARM_API_URL = 'http://docker_swarm:4000/api'
SERVICE_API_URL = 'http://service_api:5000/api'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

ROOT_URLCONF = 'homelab.urls'

WSGI_APPLICATION = 'homelab.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'homelab'),
        'USER': os.getenv('DB_USER', 'homelab_user'),
        'PASSWORD': os.getenv('DB_PASS', 'homelab_secret'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# Home Assistant Configuration
HOME_ASSISTANT_API_URL = 'http://home_assistant:8123/api/'
HOME_ASSISTANT_TOKEN = 'your_long_lived_access_token'
# Docker Swarm API URL and token
DOCKER_SWARM_API_URL = 'http://docker_swarm:4000/api'
SERVICE_API_URL = 'http://service_api:5000/api'
