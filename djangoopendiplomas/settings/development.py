from .base import *

# SECURITY WARNING: donst run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dop",
        "USER": "project",
        "PASSWORD": "project",
        "HOST": "db",
        "PORT": "5432",
    }
}
