"""
Django settings for mysite project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = os.environ.get('SECRET_KEY')
=======
SECRET_KEY = 'django-insecure-rc^*w^w&6g9_(uvx#6s*bnt!w)l0rdi%!l7mv#y%uc&x%wo5pk'
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

<<<<<<< HEAD
ALLOWED_HOSTS = ['django-6op8.up.railway.app', '.railway.app']
=======
ALLOWED_HOSTS = ["*"]
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'multas.apps.MultasConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
=======
    'multas',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5
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
<<<<<<< HEAD
        'DIRS': [],
=======
        'DIRS': [os.path.join(BASE_DIR, 'mysite/templates')],
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5
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
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
=======
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

<<<<<<< HEAD
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
=======
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
<<<<<<< HEAD
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configurações de Segurança
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True
=======
STATICFILES_DIRS = []  # Removendo diretórios adicionais para evitar duplicação
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# WhiteNoise Configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True
WHITENOISE_INDEX_FILE = True
WHITENOISE_AUTOREFRESH = True
>>>>>>> b4030ba220eb8d341c62a99b4020f00e2ed0cbf5

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
