from djangoopendiplomas.config.base import *

# SECURITY WARNING: donst run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travisdb',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dop',
            'USER': 'project',
            'PASSWORD': 'project',
            'HOST': 'db',
            'PORT': '5432',
        }
    }
