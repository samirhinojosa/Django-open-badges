from djangoopendiplomas.config.base import *

# SECURITY WARNING: donst run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if 'TRAVIS' in os.environ:
    DB_HOST = 'localhost'
else:
    DB_HOST = 'db'

DB_NAME = 'dop'
DB_USER = 'project'
DB_PASSWORD = 'project'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': f'{DB_USER}',
        'PASSWORD': DB_PASSWORD,
        'HOST': f'{DB_HOST}',
        'PORT': '5432',
    }
}
