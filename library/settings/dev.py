from base import *
import djcelery
djcelery.setup_loader()

#celery settings
BROKER_URL = 'django://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'endless_pagination',
    'envvars',
    'apps.book',
    'apps.libraryuser',
    'djcelery',
    'kombu.transport.django',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = 'staticfiles'