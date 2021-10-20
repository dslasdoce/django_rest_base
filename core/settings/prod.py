"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from core.settings.base import *
from core.settings.base_w_gcloud import *
from sentry_sdk.integrations.django import DjangoIntegration
# from firebase_admin import credentials, initialize_app
import sentry_sdk
import newrelic.agent

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your-project-name',
        'USER': 'your-user-name',
        'PASSWORD': 'your-password',
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432')
    }
}

# Setup Firebase for notification
# FIREBASE_CREDENTIALS = json.loads(os.environ.get('FIREBASE_CREDENTIALS', '{}'))
# initialize_app(credentials.Certificate(FIREBASE_CREDENTIALS))

# redis cache setup
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'temp'),
    },
    'redis': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': f'{REDIS_HOST}:{REDIS_PORT}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'MAX_ENTRIES': 5000,
        },
    },
}

# New Relic
newrelic.agent.initialize(os.path.join(BASE_DIR, 'newrelic.ini'))
