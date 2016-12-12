"""
Django settings for Discuss project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTING = ((" ".join(sys.argv)).find('manage.py test') != -1)

ALLOWED_HOSTS = ['*']
APPEND_SLASH = True
PRODUCTION = True

try:
    from .local_settings import *
except ImportError:
    pass

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True')
if DEBUG == 'False':
    DEBUG = False
else:
    DEBUG = True

DOMAIN = os.environ.get('DOMAIN', '127.0.0.1')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'NONE')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # local apps
    'users',
    'articles',

    # third part
    'rest_framework',
    'django_mobile',
    'social.apps.django_app.default',
    'actstream',
    'taggit',
    'pagedown',
    'tracking',
    'django_comments',
)

MIDDLEWARE_CLASSES = (
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.oauth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',

)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/', ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_mobile.context_processors.flavour',

                # social
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'config.context_processors.categories',
                'config.context_processors.tags',
                'config.context_processors.site_info',
            ],
            'loaders': [
                'django_mobile.loader.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'log/django.log',
        },
        # 'console': {
        #     'class': 'logging.StreamHandler',
        # },
    },
    'loggers': {
        'django': {
            'handlers': ['file',
                         # 'console'
                         ],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    },
}

# FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.TemporaryFileUploadHandler",)

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if not PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'ATOMIC_REQUESTS': True
        }
    }
else:
    DATABASES = {
        'default': {
            'NAME': os.environ.get('MYSQL_INSTANCE_NAME', 'xxx'),
            'ENGINE': 'django.db.backends.mysql',
            'USER': os.environ.get("MYSQL_USERNAME", 'xxx'),
            'PASSWORD': os.environ.get("MYSQL_PASSWORD", 'xxx'),
            'HOST': os.environ.get("MYSQL_HOST", 'xxx'),
            'PORT': os.environ.get("MYSQL_PORT", 3306),
        },
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# STATIC_URL = 'dn-stk.qbox.me/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

AUTH_USER_MODEL = 'users.User'

# QINIU
# QINIU_ACCESS_KEY = 'xxxx'
# QINIU_SECRET_KEY = 'xxxx'
# QINIU_BUCKET_NAME = 'xiaoma'
# QINIU_BUCKET_DOMAIN = 'cdn.xiaoma.wang'
# QINIU_SECURE_URL = False
# DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'


# restful
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.oauth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
}

USE_X_FORWARDED_HOST = True

# social
AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'social.backends.weibo.WeiboOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GITHUB_KEY = os.environ.get('SOCIAL_AUTH_GITHUB_KEY', 'xxx')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('SOCIAL_AUTH_GITHUB_SECRET', 'xxx')
SOCIAL_AUTH_WEIBO_KEY = os.environ.get('SOCIAL_AUTH_WEIBO_KEY', 'xxx')
SOCIAL_AUTH_WEIBO_SECRET = os.environ.get('SOCIAL_AUTH_WEIBO_SECRET', 'xxx')
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

# django activity
ACTSTREAM_SETTINGS = {
    'MANAGER': 'actstream.managers.ActionManager',
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}

# django setting
SITE_ID = 1

# paging
PAGING_SIZE = 10

# django-tracking2
TRACK_PAGEVIEWS = True

# mysocial
if PRODUCTION and not DEBUG:
    SOCIAL_CALLBACK_REDIRECT_BASE_URL = 'https://%s' % DOMAIN + '/oauth/'
else:
    SOCIAL_CALLBACK_REDIRECT_BASE_URL = 'http://%s:8000' % DOMAIN + '/oauth/'

GITHUB_SOCIAL_CALLBACK_REDIRECT_URL = SOCIAL_CALLBACK_REDIRECT_BASE_URL + 'github/'
print(GITHUB_SOCIAL_CALLBACK_REDIRECT_URL)
