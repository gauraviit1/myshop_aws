try:
	from .local import *
	live = False
except:
	live = True

import os
import dj_database_url
import psycopg2
import urllib
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if live:
	SECRET_KEY = os.environ.get('SECRET_KEY')
  # SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = True
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
    'dal',
    'dal_select2',
	'bootstrap_admin',
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
	'haystack',
	'djrichtextfield',
	# 'compressor',
	'debug_toolbar',

    'crispy_forms',
    'sorl.thumbnail',

    'shop',
	'pincodes',
    'cart',
    'orders',
    'testimonials',
    'storemaps',
)


MIDDLEWARE_CLASSES = (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

	'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware'

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
				'django.template.context_processors.media',
                'django.template.context_processors.static',
				'django.template.context_processors.tz',
                'cart.context_processors.cart',
                'shop.context_processors.bakery_items',
                'shop.context_processors.handicraft_items',
                'shop.context_processors.all_unique_products',
				'shop.context_processors.cloth_items',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
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
	AWS_PRELOAD_METADATA= True

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

	# COMPRESS_ROOT = STATIC_ROOT
	# COMPRESS_STORAGE = STATICFILES_STORAGE
	# COMPRESS_URL = STATIC_URL
	GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY')

else:
	STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
	STATIC_URL = '/static/'

	# Extra places for collectstatic to find static files.
	STATICFILES_DIRS = (
	    os.path.join(PROJECT_ROOT, 'static'),
	)


# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     # other finders..
#     'compressor.finders.CompressorFinder',
# )
# COMPRESS_ENABLED = True


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

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
LOGIN_REDIRECT_URL = '/'


DJRICHTEXTFIELD_CONFIG = {
    'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}

HTML_MINIFY = True

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

INTERNAL_IPS = ['127.0.0.1',]


PINCODE_SESSION_ID = 'pincode'
