web: gunicorn library.wsgi 
worker: python manage.py celery worker --loglevel=info
worker: python manage.py celery beat