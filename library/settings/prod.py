from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {'default': dj_database_url.config(),}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# STATIC_ROOT = 'staticfiles'

STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MANDRILL_API_KEY = "-2K3LHRupN85PP-K9ofzLg"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = "eniolaarinde1@gmail.com" 
