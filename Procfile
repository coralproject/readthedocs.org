web: gunicorn readthedocs.wsgi 0.0.0.0:8000 --log-level debug
worker: celery worker --app=readthedocs --log-level debug