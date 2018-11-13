"""Local development settings, including local_settings, if present."""
from __future__ import absolute_import
import os

from .base import CommunityBaseSettings

print('loading dev settings')

class CommunityDevSettings(CommunityBaseSettings):

    """Settings for local development"""

    PRODUCTION_DOMAIN = 'talk-documentation.herokuapp.com'
    WEBSOCKET_HOST = 'talk-documentation.herokuapp.com:8088'
    USE_SUBDOMAIN = True
    READTHEDOCS = False

    DONT_HIT_DB = False

    ACCOUNT_EMAIL_VERIFICATION = 'none'
    SESSION_COOKIE_DOMAIN = None
    CACHE_BACKEND = 'dummy://'

    SLUMBER_USERNAME = 'test'
    SLUMBER_PASSWORD = 'test'  # noqa: ignore dodgy check
    SLUMBER_API_HOST = 'talk-documentation.herokuapp.com'
    PUBLIC_API_URL = 'https://{0}'.format(PRODUCTION_DOMAIN)

    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ALWAYS_EAGER = True
    CELERY_TASK_IGNORE_RESULT = False

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    FILE_SYNCER = 'readthedocs.builds.syncers.LocalSyncer'

    # For testing locally. Put this in your /etc/hosts:
    # 127.0.0.1 test
    # and navigate to http://test:8000
    CORS_ORIGIN_WHITELIST = (
        'test:8000',
    )

    @property
    def LOGGING(self):  # noqa - avoid pep8 N802
        logging = super(CommunityDevSettings, self).LOGGING
        logging['formatters']['default']['format'] = '[%(asctime)s] ' + self.LOG_FORMAT
        # Allow Sphinx and other tools to create loggers
        logging['disable_existing_loggers'] = False
        return logging

    @property
    def DATABASES(self):  # noqa
        return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(self.SITE_ROOT, 'dev.db'),
            }
        }


CommunityDevSettings.load_settings(__name__)


import dj_database_url
DATABASES['default'] =  dj_database_url.config()

if os.environ.get('SECRET_KEY'):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # DEBUG = False

if os.environ.get('REDIS_URL'):
    REDIS_URL = os.environ.get('REDIS_URL')
    BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    SLUMBER_USERNAME = 'coraladmin'
    SLUMBER_PASSWORD = os.environ.get('SLUMBER_PASSWORD')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from .local_settings import *

# if not os.environ.get('DJANGO_SETTINGS_SKIP_LOCAL', False):
#     try:
#         # pylint: disable=unused-wildcard-import
#           # noqa
#     except ImportError:
#         pass
