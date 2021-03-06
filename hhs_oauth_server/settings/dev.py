from .base import *


# Add testac to Test environments only
if 'apps.fhir.testac' not in INSTALLED_APPS:
    INSTALLED_APPS = INSTALLED_APPS + [
        'apps.fhir.testac',
    ]

# removing security enforcement in development mode
DEBUG = True
SECRET_KEY = env('DJANGO_SECRET_KEY', '1234567890')

HOSTNAME_URL = env('HOSTNAME_URL', 'http://127.0.0.1:8000')
INVITE_REQUEST_ADMIN = env('DJANGO_INVITE_REQUEST_ADMIN', 'sales@videntity.com')

# Stub for Custom Authentication Backend
SLS_USER = env('DJANGO_SLS_USER', 'ben')
SLS_PASSWORD = env('DJANGO_SLS_PASSWORD', 'pbkdf2_sha256$24000$V6XjGqYYNGY7$13tFC13aaTohxBgP2W3glTBz6PSbQN4l6HmUtxQrUys=')
SLS_FIRST_NAME = env('DJANGO_SLS_FIRST_NAME', 'Ben')
SLS_LAST_NAME = env('DJANGO_SLS_LAST_NAME', 'Barker')
SLS_EMAIL = env('DJANGO_SLS_EMAIL', 'ben@example.com')

# overrides FHIR server configuration with fake values
FHIR_SERVER_CONF = {
    'SERVER': env('THS_FHIR_SERVER', 'http://fhir.bbonfhir.com/'),
    'PATH': env('THS_FHIR_PATH', 'fhir-p/'),
    'RELEASE': env('THS_FHIR_RELEASE', 'baseDstu2/'),
    # REWRITE_FROM should be defined as a list
    'REWRITE_FROM': env('THS_FHIR_REWRITE_FROM', ['http://ec2-52-4-198-86.compute-1.amazonaws.com:8080/baseDstu2', ]),
    'REWRITE_TO': env('THS_FHIR_REWRITE_TO', 'http://localhost:8000/bluebutton/fhir/v1'),
}
