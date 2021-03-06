"""
Django settings for freds_list project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*$7h-^y68wdaoh5!zl@es+$!4xz9r&#1!3f+r46g+*r36&tvv3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'social.apps.django_app.default',
    'bootstrap3',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework.filters',
    'corsheaders',
    'users',
    'fredslist',
    'api',

)


AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookOAuth2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'freds_list.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'freds_list.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fredslist3',
        'USER': 'cesar',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/day',
        'user': '1000/day',
        'states': '100000/day'
    },
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework_filters.backends.DjangoFilterBackend', ...
    # ),


}


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# SENDGRID_USER = os.environ['SENDGRID_USER']
# SENDGRID_PASSWORD = os.environ['SENDGRID_PASSWORD']


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
#
#
#
#
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         }
#     },
#     'handlers': {
#         'file': {
#             'level': "DEBUG",
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, "logs/general_logs.log"),
#             'formatter': 'verbose'
#         },
#         'mailer': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         }
#
#     },
#     'loggers': {
#         'chirp': {
#             'handlers': ['file', 'console', 'mailer'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#     }
#
# }
#


SOCIAL_AUTH_FACEBOOK_KEY = "1085835404768701"
SOCIAL_AUTH_FACEBOOK_SECRET = "158c19308bc19e38bbbbff2df1051ab2"

SOCIAL_AUTH_TWITTER_KEY = 'wgnRgPMEGVW4B8AcgBHh07x0U'
SOCIAL_AUTH_TWITTER_SECRET = 't0yiUinbdK4PIybSODPdvmWTSRLpLjIprQkd3KUwTd6yz4mV1e'
