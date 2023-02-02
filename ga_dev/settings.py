
"""
Django settings for ga_dev project.
Generated by 'django-admin startproject' using Django 4.1.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from email.policy import default
import os
from pickle import TRUE
from django.test.runner import DiscoverRunner
from decouple import config

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
IS_HEROKU = "DYNO" in os.environ
APPEND_SLASH=False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY= config("SECRET_KEY")

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

if IS_HEROKU:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = []
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TRUE

ALLOWED_HOSTS = ["ga-devs1.herokuapp.com","127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usarios.apps.UsariosConfig'
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

ROOT_URLCONF = 'ga_dev.urls'

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

WSGI_APPLICATION = 'ga_dev.wsgi.application'
MAX_CONN_AGE = 600


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES= {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'DATABASE':"derv8pabfd08tc",
        'USER': 'cnjyhtpzalzrxx',
        'HOST': 'ec2-3-209-124-113.compute-1.amazonaws.com',
        'PORTS': "5432",
        'PASSWORD':"5b240f72baa13aa11131ab02f1c06fe017ff1d6059a903faf23c2cf512dd772e",
        # 'PASSWORD': config('PASSWORD'),
        "URI": "postgres://cnjyhtpzalzrxx:5b240f72baa13aa11131ab02f1c06fe017ff1d6059a903faf23c2cf512dd772e@ec2-3-209-124-113.compute-1.amazonaws.com:5432/derv8pabfd08tc"
    }
}


import dj_database_url
# if "DATABASE_URL" in os.environ:
# #     # Configure Django for DATABASE_URL environment variable.
#     DATABASES["default"] = dj_database_url.config(
#         conn_max_age=MAX_CONN_AGE, ssl_require=True)

#     # Enable test database if found in CI environment.
#     if "CI" in os.environ:
#         DATABASES["default"]["TEST"] = DATABASES["default"]

# if IS_HEROKU: 
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


#     DATABASE_URL='postgresql://wilmerbaby:ratachanga@database-1.cuctlgmeb8x4.us-east-1.rds.amazonaws.com:5432/needed'
# else:
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)
# DATABASE_URL='sqlite:///'+ os.path.join(BASE_DIR,'db.sqlite3')    
# DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# # db_from_env = dj_database_url.config(conn_max_age=600)
# # DATABASES['default'].update(db_from_env)

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

# <?xml version="1.0" encoding="UTF-8"?>
# <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
# <CORSRule>
#   <AllowedOrigin>*</AllowedOrigin>
#   <AllowedMethod>GET</AllowedMethod>
#   <AllowedMethod>HEAD</AllowedMethod>
#   <MaxAgeSeconds>3000</MaxAgeSeconds>
#   <AllowedHeader>*</AllowedHeader>
# </CORSRule>
# </CORSConfiguration> 

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
class HerokuDiscoverRunner(DiscoverRunner):
    """Test Runner for Heroku CI, which provides a database for you.
    This requires you to set the TEST database (done for you by settings().)"""

    def setup_databases(self, **kwargs):
        self.keepdb = True
        return super(HerokuDiscoverRunner, self).setup_databases(**kwargs)


# Use HerokuDiscoverRunner on Heroku CI
if "CI" in os.environ:
    TEST_RUNNER = "gettingstarted.settings.HerokuDiscoverRunner"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'