import os
print('loading local settings')
DEBUG = False

SECRET_KEY = 'no really its a secret' 

PRODUCTION_DOMAIN = 'talk-documentation.herokuapp.com:8000'
WEBSOCKET_HOST = 'talk-documentation.herokuapp.com:8088'

import django_heroku


# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=600)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd8d4roi3skj3gl',
#         'USER': 'utapyfvsbflzuj',
#         'PASSWORD': '082e68c88f087bb54d9f390607c0279b109888a7815f3d227d7d213cad72c31c',
#         'HOST': 'ec2-184-73-197-211.compute-1.amazonaws.com',
#         'PORT': '5432',                      
#     }
# }


# DATABASES['default'] =  dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

django_heroku.settings(locals())