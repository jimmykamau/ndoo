"""
Production specific settings for ndoo project.
"""

from .base import *
import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']
