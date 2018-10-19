import os
print('loading local settings')
DEBUG = False

SECRET_KEY = 'no really its a secret' 

PRODUCTION_DOMAIN = 'talk-documentation.herokuapp.com:8000'
WEBSOCKET_HOST = 'talk-documentation.herokuapp.com:8088'

ADMINS = (
        ('Jessie Rushing', 'jessiekrushing@gmail.com'),
    )

SESSION_COOKIE_DOMAIN = 'docs.coralproject.net'



import django_heroku
import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',       
    }
}


DATABASES['default'] =  dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

django_heroku.settings(locals())