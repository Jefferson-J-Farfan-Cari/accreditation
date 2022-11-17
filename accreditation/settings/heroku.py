from accreditation.settings import *

import django_heroku

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
]

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

# Settings for Django
INSTALLED_APPS = FIRST_APPS + OWN_APPS + THIRD_APPS

django_heroku.settings(locals())
