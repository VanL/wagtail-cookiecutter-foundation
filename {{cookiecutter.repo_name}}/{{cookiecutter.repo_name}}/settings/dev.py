from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
SECRET_KEY = '7nn(g(lb*8!r_+cc3m8bjxm#xu!q)6fidwgg&$p$6a+alm+eex'
DATABASES['default']['PASSWORD'] = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Process all tasks synchronously.
# Helpful for local development and running tests
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True

try:
    from .local import *
except ImportError:
    pass
