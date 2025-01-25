import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'why-this-key-is-not-fetched-from-env')

DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ["0.0.0.0", "localhost"]

INSTALLED_APPS = [
    # default django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # newly created apps
    'userauths',
    'channel',
    'core',
    "taggit",
    'useradmin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ytprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'ytprj.wsgi.application'

# moving DB from sqlite to postgres :)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'db-name'),
        'USER': os.environ.get('DATABASE_USER', 'db-user'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'db-password'),
        'HOST': os.environ.get('DATABASE_HOST', 'db-host'),
        'PORT': os.environ.get('DATABASE_PORT', 5432)
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


MEDIA_URL= '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
    
if not DEBUG:
    STATIC_ROOT = ''
    
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

# email verfications
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'djangowork97@gmail.com'
EMAIL_HOST_PASSWORD = 'qcntouxmmitgjdyu'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS= {
    "site_title":"Youtube Studio",
    "site_header":"Youtube Studio",
    "site_brand":"Think | Create | Inspire",
    "site_logo" : "images/youtube-icon.svg",
    # "copyright":"All rights are reserved to Brij.ai"
    
}
