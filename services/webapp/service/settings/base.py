import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta

from service.settings.connections.aws import AWS
from service.settings.connections.elasticache import Redis, SmartCache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.main'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'

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

WSGI_APPLICATION = 'service.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}

DEPLOYED = False
STACK = os.environ.get('DJANGO_SETTINGS_MODULE', 'service.settings.local').split('.')[-1]
LOCALSTACK = True if STACK == 'local' else False
if LOCALSTACK and not os.environ.get("DOCKERIZED", False):
    from utils.local_env import set_env_vars
    set_env_vars()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
AWS_REGION_NAME = os.environ['AWS_REGION']
USER_SEARCH_AGE_OFF = timedelta(weeks=2)
USER_SEARCH_AGE_OFF_SECONDS = int(USER_SEARCH_AGE_OFF.total_seconds())
TFID_AGE_OFF = 3600 * 2  # 2 hours
MAX_SEARCH_RADIUS = 16093  # 10 Miles

# Services
SSM = AWS.client('ssm', localstack=LOCALSTACK,
                 region_name=AWS_REGION_NAME,
                 host=os.environ['LOCALSTACK_HOST'],
                 port=os.environ['LOCALSTACK_PORT'])
DYNAMODB = AWS.client('dynamodb', localstack=LOCALSTACK,
                      region_name=AWS_REGION_NAME,
                      host=os.environ['LOCALSTACK_HOST'],
                      port=os.environ['LOCALSTACK_PORT'])
REDIS = Redis()
SMART_CACHE = SmartCache(REDIS)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['POSTGRES_SCHEMA'],
        'USER': os.environ['POSTGRES_USER'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PASSWORD': os.environ['POSTGRES_PASS'],
        'PORT': os.environ['POSTGRES_PORT'],
        # 'CONN_MAX_AGE': 300
    },
}
