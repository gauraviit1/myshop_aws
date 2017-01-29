try:
	from .local import *
	live = False
except:
	live = True

import os
import dj_database_url
import psycopg2
import urllib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if live:
	SECRET_KEY = os.environ.get('SECRET_KEY')
  # SECURITY WARNING: don't run with debug turned on in production!
	DEBUG =True
	TEMPLATE_DEBUG = True


else:
  # SECURITY WARNING: keep the secret key used in production secret!
	SECRET_KEY = '-8g=-r5j_h%3njm!$un3u2owe3xf#(aymj)+(jhl0)1*ap!6overmagauravvermagarima'
	DEBUG = True
	TEMPLATE_DEBUG = True


# Allow all host headers
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    # 'dal',
    # 'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.postgres',
    'storages',
    'mptt',
    'django_mptt_admin',

    'crispy_forms',
    'sorl.thumbnail',
    'shop',
    'cart',
    'orders',
    'testimonials',
    'storemaps',
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
)

ROOT_URLCONF = 'myshop.urls'


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
                'cart.context_processors.cart',
                'shop.context_processors.bakery_items',
                'shop.context_processors.handicraft_items',
                'shop.context_processors.all_unique_products',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

if live:
	DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': '',
      'USER': '',
      'PASSWORD': '',
      'HOST': '',
      'PORT': '',
  }
}




	urllib.parse.uses_netloc.append("postgres",)
	url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(
	    database=url.path[1:],
	    user=url.username,
	    password=url.password,
	    host=url.hostname,
	    port=url.port
	)

	DATABASES['default'] =  dj_database_url.config()
	# Update database configuration with $DATABASE_URL.
	db_from_env = dj_database_url.config(conn_max_age=500)
	DATABASES['default'].update(db_from_env)

else:

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql',
	        'NAME': 'postgres',
	        'USER': 'postgres',
	        'PASSWORD': 'gaurav',
	        'HOST': '',
	        'PORT': '5432',
	    }
	}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
if live:
	STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
	STATIC_URL = '/static/'

	# Extra places for collectstatic to find static files.
	STATICFILES_DIRS = (
	    os.path.join(PROJECT_ROOT, 'static'),
	)

	AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

	AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

	AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

	AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

	STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
	# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

	AWS_S3_HOST = 's3-ap-south-1.amazonaws.com'

	os.environ['S3_USE_SIGV4'] = 'True'


	STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/' + 'static/'

	# DO NOT DO THIS!
	MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
	DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

	# STATIC_URL = 'http://s3.amazonaws.com/'  + AWS_STORAGE_BUCKET_NAME +"/"
	ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

else:
	STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
	STATIC_URL = '/static/'

	# Extra places for collectstatic to find static files.
	STATICFILES_DIRS = (
	    os.path.join(PROJECT_ROOT, 'static'),
	)


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CART_SESSION_ID = 'cart'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'mcjail.shi.hp@gmail.com'

if live:
	EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

EMAIL_PORT = 587

EMAIL_USE_TLS = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'
