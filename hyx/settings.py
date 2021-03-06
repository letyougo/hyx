"""
Django settings for hyx project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import socket

hostname = socket.gethostname()



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#6z*9+qx-wowu#%6eg40cc+v$(za6y9jdo1%!vqom42&j_*^t*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if hostname=='suruideiMac.local' else False

DEBUG = True

ALLOWED_HOSTS = [
    '101.200.129.112',
    'localhost',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ky.apps.KyConfig',

]

MIDDLEWARE = [
  
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hyx.urls'

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

WSGI_APPLICATION = 'hyx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jk',
        'USER': 'root',
        'PASSWORD': 'surui123',
        'HOST': '101.200.129.112',
        # 'HOST': 'localhost',
        'PORT': '3306',
    }
}


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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = '/login/'


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),

)
APPEND_SLASH=False



PAGE_SIZE = 10
PAGE_NUM = 1

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:9999',
    '127.0.0.1:9000'
)


LOGGING2 = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True,
            },
            'default': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR,'logs','all.log'),     #日志输出文件
                'maxBytes': 1024*1024*5,                  #文件大小
                'backupCount': 5,                         #备份份数
                'formatter':'standard',                   #使用哪种formatters日志格式
            },
            'error': {
                'level':'ERROR',
                'class':'logging.handlers.RotatingFileHandler',
                'filename':os.path.join(BASE_DIR,'logs','error.log'),
                'maxBytes':1024*1024*5,
                'backupCount': 5,
                'formatter':'standard',
            },
            'console':{
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'request_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR,'logs','request.log'),
                'maxBytes': 1024*1024*5,
                'backupCount': 5,
                'formatter':'standard',
            },
            'scprits_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename':os.path.join(BASE_DIR,'logs','scripts.log'),
                'maxBytes': 1024*1024*5,
                'backupCount': 5,
                'formatter':'standard',
            },

            'db': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(BASE_DIR,'logs','db.log'),
                'formatter': 'standard'
            },  # 用于文件输出
        },

        'loggers': {
            'django.db.backends': {
                'handlers': ['db','console'],
                'level': 'DEBUG' if DEBUG else 'INFO',
            },
            # 'django': {
            #     'handlers': ['default', 'console'],
            #     'level': 'DEBUG',
            #     'propagate': False
            # },
            # 'django.request': {
            #     'handlers': ['request_handler'],
            #     'level': 'DEBUG',
            #     'propagate': False,
            # },
            # 'scripts': {
            #     'handlers': ['scprits_handler'],
            #     'level': 'INFO',
            #     'propagate': False
            # },
            # 'sourceDns.webdns.views': {
            #     'handlers': ['default', 'error'],
            #     'level': 'DEBUG',
            #     'propagate': True
            # },
            # 'sourceDns.webdns.util':{
            #     'handlers': ['error'],
            #     'level': 'ERROR',
            #     'propagate': True
            # }
    },
}
LOGIN_URL='/login/'