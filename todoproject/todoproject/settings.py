import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug mode (set to False in production)
DEBUG = False

# Allowed hosts (update this for production)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Root URL configuration
ROOT_URLCONF = 'todoproject.urls'

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'corsheaders',  # CORS middleware if needed
    'todoapp',  # Your custom app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  # Enable this for general middleware
    'corsheaders.middleware.CorsMiddleware',  # Enable if using CORS
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templates
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

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_db',  # Replace with your PostgreSQL database name
        'USER': 'arif',  # Your PostgreSQL username
        'PASSWORD': 'arif',  # Your PostgreSQL password
        'HOST': 'localhost',  # Keep this if using local database
        'PORT': '5432',  # Default PostgreSQL port
    }
}

SECRET_KEY = 'swkbioku0-8bz!@y6@(1bmexz%6vxt+@6yfgczi6%fw@_z*982'

# Static files configuration
STATIC_URL = '/static/'

# Directory where static files are collected
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional directories for static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Custom static directory in your project
]

# CORS settings (if needed)
CORS_ALLOW_ALL_ORIGINS = True

# Logging (optional, useful for debugging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
