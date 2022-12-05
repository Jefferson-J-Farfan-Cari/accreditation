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
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

# Applications
OWN_APPS = [
    'apps.base',
    'apps.user',
    'apps.course',
    'apps.student',
    'apps.portafolio',
    'apps.forms',
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

# Settings for Swagger
SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}
