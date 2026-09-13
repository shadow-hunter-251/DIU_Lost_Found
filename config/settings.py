from pathlib import Path

import os

from dotenv import load_dotenv



BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')



# SECURITY

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-development-key'
)

DEBUG = os.getenv(
    'DEBUG',
    'False'
) == 'True'


if not DEBUG:

    SECURE_SSL_REDIRECT = True
    
    SESSION_COOKIE_SECURE = True
    
    CSRF_COOKIE_SECURE = True
    
    SECURE_CONTENT_TYPE_NOSNIFF = True
    
    X_FRAME_OPTIONS = 'DENY' == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

CSRF_TRUSTED_ORIGINS = []

# LOGIN

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'



# APPLICATIONS

INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'rest_framework',

    'rest_framework.authtoken',

    'tailwind',

    'theme',

    'django_browser_reload',

    'accounts',

    'items',

    'claims',

    'notifications',

    'dashboard',

    'api',

    'matching',

]



# MIDDLEWARE

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



# URL

ROOT_URLCONF = 'config.urls'



# TEMPLATES

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [

            BASE_DIR / 'templates',

        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]



# WSGI

WSGI_APPLICATION = 'config.wsgi.application'



# DATABASE

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'diu_lost_found',

        'USER': 'root',

        'PASSWORD': '1234',

        'HOST': 'localhost',

        'PORT': '3300',

    }

}



# PASSWORD VALIDATION

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



# LANGUAGE

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# STATIC FILES

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'



# MEDIA FILES

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'



# DEFAULT PRIMARY KEY

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# TAILWIND

TAILWIND_APP_NAME = 'theme'

NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'



# REST FRAMEWORK

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [

        'rest_framework.authentication.TokenAuthentication',

        'rest_framework.authentication.SessionAuthentication',

    ],

    'DEFAULT_PERMISSION_CLASSES': [

        'rest_framework.permissions.AllowAny',

    ],

}

# SECURITY

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-development-key'
)

DEBUG = os.getenv(
    'DEBUG',
    'False'
) == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


CSRF_TRUSTED_ORIGINS = []


# PRODUCTION SECURITY

if not DEBUG:

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = 'DENY'