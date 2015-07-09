from .base import *

import djrill

DEBUG = True

# Application definition

MANDRILL_API_KEY = "-2K3LHRupN85PP-K9ofzLg"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = "eniolaarinde1@gmail.com" 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = 'staticfiles'