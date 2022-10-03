from accreditation.settings import *

# Frameworks
THIRD_APPS = [
    'rest_framework',
    'corsheaders',
    'simple_history'
]
# Applications
OWN_APPS = [
]
# Settings for Django
INSTALLED_APPS = FIRST_APPS + OWN_APPS + THIRD_APPS
