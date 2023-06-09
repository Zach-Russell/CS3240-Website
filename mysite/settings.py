"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0l)-#&@61_nyqaefbce@cex3+)#8c-td#5o7j-tpe*96z0i_kb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','a25.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'welcome.apps.WelcomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap5',
]

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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases



#Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

#Redirect HTTP -> HTTPS
SECURE_SSL_REDIRECT = True

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':'d8iceoto8h3b8r',      
      'USER':'lxbfwhwbnrjsrs',     
      'PASSWORD':'a6f7d246548b7725076674c3b52d69f031e9ff37a295a59cd2a98f00a565555f',
      'HOST':'ec2-52-71-23-11.compute-1.amazonaws.com',
      'PORT':'5432',
      'TEST' : {
            'MIRROR' : 'default',
      },
      
   }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = '/media/' 
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Activate Django-Heroku.
# Use this code to avoid the psycopg2 / django-heroku error!  
# Do NOT import django-heroku above!
try:
    if 'HEROKU' in os.environ:
        import django_heroku
        django_heroku.settings(locals())
except ImportError:
    found = False


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_FORMS = {'login': 'welcome.forms.MyCustomLoginForm',
                 'signup': 'welcome.forms.MyCustomSignupForm'}
SOCIALACCOUNT_FORMS = {'signup': 'welcome.forms.MyCustomSocialSignupForm'}
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": '352649337280-qk5q7p74a4v3alhlufjd0inols4tdq9s.apps.googleusercontent.com',
            "secret": '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',
            "key": ""
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_ADAPTER = 'welcome.adapters.MyAccountAdapter'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION ="none"
AUTH_USER_MODEL = 'welcome.User'
SOCIALACCOUNT_LOGIN_ON_GET=True
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# EMAIL_HOST_USER = 'tutormedjango@gmail.com'
# EMAIL_HOST_PASSWORD = 'admin123!'

# django_project/settings.py
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  
EMAIL_HOST = "smtp.sendgrid.net"  
EMAIL_HOST_USER = "apikey"  
EMAIL_HOST_PASSWORD = "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"  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True  
