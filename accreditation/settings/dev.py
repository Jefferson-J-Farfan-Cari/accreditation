from accreditation.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# CORS CONFIG
CORS_ORIGIN_ALLOW_ALL = True

# Frameworks
THIRD_APPS = [
    'rest_framework',
    'django_filters',
    'corsheaders',
    'drf_yasg',
    'simple_history',
]

# Applications
OWN_APPS = [
    'apps.base',
    'apps.user'
]

# Settings for Django
INSTALLED_APPS = FIRST_APPS + OWN_APPS + THIRD_APPS

# Database Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3',
    }
}
