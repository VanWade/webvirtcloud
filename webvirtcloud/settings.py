"""
Django settings for webvirtcloud project.

"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '4y(f4rfqc6f2!i8_vfuu)kav6tdv5#sc=n%o451dm+th0&3uci'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'computes',
    'console',
    'networks',
    'storages',
    'interfaces',
    'instances',
    'secrets',
    'logs',
    'accounts',
    'create',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.RemoteUserBackend',
#    #'accounts.backends.MyRemoteUserBackend',
#)

LOGIN_URL = '/accounts/login'

ROOT_URLCONF = 'webvirtcloud.urls'

WSGI_APPLICATION = 'webvirtcloud.wsgi.application'

DATABASES = {
    'default': {
        'NAME': 'kvmmgr',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'Czn@0011',
        'HOST': '192.168.16.158',
        'PORT': '3306'
    }
}
# Cache
CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'default',
    # }
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

## WebVirtCloud settings

# Wobsock port
WS_PORT = 6080

# Websock host
WS_HOST = '0.0.0.0'

# Websock public port
WS_PUBLIC_HOST = None

# Websock SSL connection
WS_CERT = None

# list of console types
QEMU_CONSOLE_TYPES = ['vnc', 'spice']

# default console type
QEMU_CONSOLE_DEFAULT_TYPE = 'vnc'

# list taken from http://qemu.weilnetz.de/qemu-doc.html#sec_005finvocation
QEMU_KEYMAPS = ['ar', 'da', 'de', 'de-ch', 'en-gb', 'en-us', 'es', 'et', 'fi',
                'fo', 'fr', 'fr-be', 'fr-ca', 'fr-ch', 'hr', 'hu', 'is', 'it',
                'ja', 'lt', 'lv', 'mk', 'nl', 'nl-be', 'no', 'pl', 'pt',
                'pt-br', 'ru', 'sl', 'sv', 'th', 'tr']

# keepalive interval and count for libvirt connections
LIBVIRT_KEEPALIVE_INTERVAL = 5
LIBVIRT_KEEPALIVE_COUNT = 5

ALLOW_INSTANCE_MULTIPLE_OWNER = True
CLONE_INSTANCE_DEFAULT_PREFIX = 'ourea'
LOGS_PER_PAGE = 100
QUOTA_DEBUG = True
ALLOW_EMPTY_PASSWORD = True

# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULE = {
    # 'test_print': {
    #     'schedule': 3.0,
    #     'task': 'instances.tasks.test_print'
    # }
    # 'test_logger': {
    #     'schedule': 3.0,
    #     'task': 'instances.tasks.test_logger'
    # }
    'update_kvm_status': {
        'schedule': 60.0,
        'task': 'instances.tasks.update_kvm_status'
    }
}