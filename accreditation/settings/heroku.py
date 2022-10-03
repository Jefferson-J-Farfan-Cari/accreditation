from accreditation.settings import *

import django_heroku

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

django_heroku.settings(locals())
