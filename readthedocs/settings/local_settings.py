import os

SECRET_KEY = 'no really its a secret' 

PRODUCTION_DOMAIN = 'talk-documentation.herokuapp.com:8000'
WEBSOCKET_HOST = 'talk-documentation.herokuapp.com:8088'

import django_heroku
django_heroku.settings(locals())


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES[‘default’].update(db_from_env)
