"""
Django settings for IDS_GraphQL project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-)0e5be#9fv9z-)8m_ns_r!&jugs$djcs9l7twx(0c5abuuf3oc'

# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-)0e5be#9fv9z-)8m_ns_r!&jugs$djcs9l7twx(0c5abuuf3oc')
# JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '9a9d6ca22c332fd00c445fbabb3b55c73f52cbf3a690ac388d2b08ded3aadabc')

SECRET_KEY='W2IjUe3kllnnZGWGDnRj8R3EukdojlSM8OlLUIJSvkA'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #installed_apps
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    #local_apps
    'Authentication',
    'Core',
    'Object_Detection',
    'idscore'
    
    # 'graphql_auth',
    # 'graphql_jwt',
    

]
AUTH_USER_MODEL='Authentication.Login'
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'Authentication.middlewares.CustomJWTMiddleware',


]

# CSRF_COOKIE_NAME = "csrf"


ROOT_URLCONF = 'IDS_GraphQL.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'IDS_GraphQL.wsgi.application'



GRAPHENE = {
    'SCHEMA': 'IDS_GraphQL.schema.schema',  # Update with your project name
       "MIDDLEWARE": [
            "graphql_jwt.middleware.JSONWebTokenMiddleware",
       ],
}



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ides_productdetails',
        'USER': 'suvarna',
        'PASSWORD': 'WtP73JWm7n1DOlCcVAsdngc7xL9DNf5C',
        'HOST': 'dpg-cplbrp0cmk4c739lfam0-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import datetime
GRAPHQL_JWT = {
    'JWT_PAYLOAD_HANDLER': 'IDS_GraphQL.utils.jwt_payload',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),    
    'JWT_SECRET_KEY': 'W2IjUe3kllnnZGWGDnRj8R3EukdojlSM8OlLUIJSvkA',
    'JWT_ALGORITHM': 'HS256',
}

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# GRAPHQL_JWT = {
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',
# }

# GRAPHQL_JWT = {
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=60),  # adjust as needed
# }

# GRAPHQL_JWT = {
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_SECRET_KEY': 'W2IjUe3kllnnZGWGDnRj8R3EukdojlSM8OlLUIJSvkA',
#     # 'JWT_PAYLOAD_HANDLER': 'graphql_jwt.utils.jwt_payload',

# }

# # JWT settings
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
#     'JWT_ALLOW_REFRESH': True,
# }