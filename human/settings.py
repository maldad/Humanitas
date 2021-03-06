"""
Django settings for human project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f)#pfs^$*6&x$2k1##*_gj-xoi5&7h69ux)77^4copvjbekml*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'escuela',
)

TEMPLATE_DIRS = (
    '/home/maldad/Documentos/ing_software/humanitas2/templates/',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'human.urls'

WSGI_APPLICATION = 'human.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_ROOT = '/home/maldad/Documentos/ing_software/humanitas2/static/static_root/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    #'/home/maldad/Documentos/ing_software/humanitas2/static/static_dirs/',
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)
#MEDIA_ROOT = '/home/maldad/Documentos/ing_software/humanitas2/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
MEDIA_URL = '/media/'
