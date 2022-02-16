"""
Django settings for MarketPlace project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n%&o3f!xv8w^#0vn-axhw$-e_o%c!!d&%7qfkn#_zp60j5vdt+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STRIPE_PUB_KEY = 'pk_test_51JOcmWAtK8R4fpfXcp9NpjJ0ZgOtmP1c26xAMUdGtY9Xjad4tcxwEXQVzHXxDqctsqKeh6BGk3tOSuj19ac3CNq300WL2BC4gD'
STRIPE_SECRET_KEY = 'sk_test_51JOcmWAtK8R4fpfXdPJZRxgDIbzH5iV5qKx0JWtgQIqhpUvWJ9QvW6b8jvFg9BQLxxEFNgDvOtBv6EQIPCVQ7Jvk00nsqjtEvi'

LOGIN_URL= 'ingresar'
LOGIN_REDIRECT_URL= 'usuarioadmin'
LOGOUT_REDIRECT_URL= 'principal'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587 
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = 'Marketplace <jhandry.lapo@unledu.ec>'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'AppHome',
    'crispy_forms',
    'AppOrder',
    'AppCarrito',
    'AppUsuario',
    'AppProducto',
    'corsheaders',
]


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'MarketPlace.urls'

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
                'AppProducto.context_processors.menu_categorias',
                'AppCarrito.context_processors.carrito'
            ],
        },
    },
]

WSGI_APPLICATION = 'MarketPlace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =  [
    BASE_DIR / 'static'
]



MEDIA_URL= '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'