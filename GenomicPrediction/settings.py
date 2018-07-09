"""
Django settings for GenomicPrediction project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'y1&h&rarxr(w&+7rdq5^3uvwru_-4$7g4tqfrefkp218(jbu(8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True
# TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GenomicPrediction.settings.local')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SimpleShop',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'GenomicPrediction.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'GenomicPrediction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'GenomicPrediction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'OPTIONS': {
    #             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #         },
    #         'NAME': os.environ['DATABASE_NAME'],
    #         'HOST': os.environ['DATABASE_HOST'],
    #         'PORT': os.environ['DATABASE_PORT'],
    #         'USER': os.environ['DATABASE_USER'],
    #         'PASSWORD': os.environ['DATABASE_PASSWORD'],
    #     }}

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'NAME': 'simpleshop',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': 'visasept17',
        }}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Message Tags


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "SimpleShop/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

LOGIN_EXEMPT_URLS = (
 r'^login/',
 r'^admin/',
)

LOGOUT_REDIRECT_URL = '/'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'qiaoweitang'
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

EMAIL_HOST_PASSWORD = 'visasept17'
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

EMAIL_PORT = 587
EMAIL_USE_TLS = True


# AWS Credentials
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_ACCESS_KEY_ID = 'AKIAJTTA267CONB3FMNQ'
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = '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'
# Celery

BROKER_URL = "sqs://%s:%s@" % (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_DEFAULT_QUEUE = 'simpleshopemail'
CELERY_RESULT_BACKEND = None # Disabling the results backend
CELERY_IMPORTS = ['SimpleShop.tasks']
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-west-2',
    'polling_interval': 20,
}