# Django settings for america project.

import os

import dj_database_url
from lib.S3 import CallingFormat

SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
     ('Kenneth Kay', 'ken.kay@icihere.com'),
     ('David Y. Kay', 'dk@gargoyle.co'),
)

MANAGERS = ADMINS

if os.environ.get('ENVIRONMENT') == 'production':
  DEBUG = False
  DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
  #EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

  MEDIA_ROOT  = 'media/'
  STATIC_ROOT = ''

  MEDIA_URL  = 'http://media.toamerica.us/media/'
  STATIC_URL = 'http://media.toamerica.us/'

  AWS_BUCKET_NAME = 'media.toamerica.us'   # Bucket name
  # BOTO
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
  AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
  AWS_STORAGE_BUCKET_NAME = AWS_BUCKET_NAME
else:
  DEBUG = True
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'america',
          'USER': '',
          'PASSWORD': '',
          'HOST': '',
          'PORT': '',
      }
  }
  STATIC_ROOT = SITE_ROOT + '/static/'
  STATIC_URL = '/static/'
  # Absolute filesystem path to the directory that will hold user-uploaded files.
  # Example: "/home/media/media.lawrence.com/media/"
  MEDIA_ROOT = SITE_ROOT + '/media/'

  # URL that handles the media served from MEDIA_ROOT. Make sure to use a
  # trailing slash.
  # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
  MEDIA_URL = ''

# TODO: Bifurcate this for production!
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Additional locations of static files
STATICFILES_DIRS = (
    SITE_ROOT + '/static_storage/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zt-l!02u!zaib!9fh)-y_wwq=zom0b02r927f-!g2ij4%bmom4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'america.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'america.wsgi.application'

TEMPLATE_DIRS = (
    SITE_ROOT + '/templates/',
    # Don't forget to use absolute paths, not relative paths.
)

#AUTH_PROFILE_MODULE = ''

#AUTHENTICATION_BACKENDS = (
#    'userena.backends.UserenaAuthenticationBackend',
#    'guardian.backends.ObjectPermissionBackend',
#    'django.contrib.auth.backends.ModelBackend',
#    )

PAYPAL_RECEIVER_EMAIL = ''

INSTALLED_APPS = (
    # Our App
    'america.catalog',
    'america.accounts',

    # Third-Party
    'south',
    'easy_thumbnails',
    'paypal.standard.ipn',
    #'userena',
    #'guardian',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
