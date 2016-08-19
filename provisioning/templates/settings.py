"""
Django settings for scoutproject project.

Generated by 'django-admin startproject' using Django 1.8.4.

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
SECRET_KEY = '{{ settings_secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = (
    '127.0.0.1',
    '0.0.0.0', #add your server's ip address!
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scout',
    'scout_manager',
    'hybridize',
    'turbolinks',
    'spotseeker_restclient',
    'compressor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
    'turbolinks.middleware.TurbolinksMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)

ROOT_URLCONF = 'scoutproject.urls'

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
                'scout.context_processors.google_maps',
                'scout.context_processors.google_analytics',
                'scout.context_processors.is_desktop',
                'scout.context_processors.is_hybrid',
            ],
        },
    },
]

WSGI_APPLICATION = 'scoutproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
STATIC_ROOT = '/tmp/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/home/vagrant/scout.log',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


# django mobileesp

from django_mobileesp.detector import mobileesp_agent as agent

DETECT_USER_AGENTS = {

    'is_tablet' : agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,

    'is_and': agent.detectAndroid,
    'is_ios': agent.detectIos,
    'is_win': agent.detectWindowsPhone,
}

COMPRESS_ROOT = "/tmp/"
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'pyscss {infile} > {outfile}'),
    ('text/x-scss', 'pyscss {infile} > {outfile}'),
)
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_OUTPUT_DIR = ''
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

# google analytics
#GOOGLE_ANALYTICS_KEY = "UA-XXXXXXXX-X"

# htmlmin
HTML_MINIFY = True

# spotseeker-test api
SPOTSEEKER_HOST = ""
SPOTSEEKER_OAUTH_KEY = ""
SPOTSEEKER_OAUTH_SECRET = ""
#SPOTSEEKER_DAO_CLASS = "spotseeker_restclient.dao_implementation.spotseeker.Live"

# saucelabs
#SAUCE_USERNAME = ''
#SAUCE_ACCESS_KEY = ''

# scout manager
#SCOUT_MGR_BRANDING = True
