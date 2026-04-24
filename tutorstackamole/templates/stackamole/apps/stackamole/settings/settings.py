import json
import os

from distutils.util import strtobool


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = "{{ STACKAMOLE_SECRET_KEY }}"
DEBUG = bool(strtobool("{{ STACKAMOLE_DEBUG }}"))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s:%(name)s:%(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING'
    },
}

ALLOWED_HOSTS = ["{{ LMS_HOST }}"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "{{ OPENEDX_MYSQL_DATABASE }}",
        'USER': "{{ OPENEDX_MYSQL_USERNAME }}",
        'PASSWORD': "{{ OPENEDX_MYSQL_PASSWORD }}",
        'HOST': "{{ MYSQL_HOST }}",
        'PORT': "{{ MYSQL_PORT }}",
        'ATOMIC_REQUESTS': False,
        'CONN_MAX_AGE': 0,
        'OPTIONS': {},
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'stackamole_guacamole_client'
]

ASGI_APPLICATION = 'stackamole_guacamole_client.asgi:application'

XBLOCK_SETTINGS = {
    "stackamole": json.loads(
        """{{ STACKAMOLE_XBLOCK_SETTINGS | tojson(indent=4) }}""")
}
