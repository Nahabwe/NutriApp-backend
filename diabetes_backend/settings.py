

from pathlib import Path
from datetime import timedelta
import os
import environ
import logging

env =environ.Env(
    DEBUG=(bool,False)
)
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR,'.env'))
# Build paths inside the project like this: BASE_DIR / 'subdir'.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #3rd parties app
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'api',
    'drf_yasg',
]

REST_FRAMEWORK = {

'DEFAULT_PERMISSION_CLASSES':[
    
    'rest_framework.permissions.IsAuthenticated'
    ],

     'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

    
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),  
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

DJOSER = {
    'LOGIN_FIELD': 'username',  # or 'email' if you use email
    'USER_CREATE_PASSWORD_RETYPE': True,  # optional: require password confirmation
    'SERIALIZERS': {
        'user_create': 'djoser.serializers.UserCreateSerializer',
        'user': 'djoser.serializers.UserSerializer',
        'current_user': 'djoser.serializers.UserSerializer',
    },
    'PERMISSIONS': {
       'user_create': ['rest_framework.permissions.AllowAny'],  # ✅ allow anyone to sign up
        'user': ['rest_framework.permissions.IsAuthenticated'],
        'user_list': ['rest_framework.permissions.IsAdminUser'],
        'user_delete': ['rest_framework.permissions.IsAuthenticated'],
    },
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]


CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'diabetes_backend.urls'

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

WSGI_APPLICATION = 'diabetes_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


#local development database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': 'Nahabwe$diabetesdb1',
#         'NAME': 'diabetesdb',
#         'USER': 'Nahabwe',
#         'PASSWORD': 'Favour2323?',
#         # 'HOST': 'Nahabwe.mysql.pythonanywhere-services.com',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Nahabwe$diabetesdb1',
        'USER': 'Nahabwe',
        'PASSWORD': 'Favour2323?',
        'HOST': 'Nahabwe.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT= BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




                         
# ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME'), 'localhost','127.0.0.1','localhost:5173', 'localhost:3000', 'localhost:8000', ]

ALLOWED_HOSTS = [
    'web-production-2e69c.up.railway.app',
    'localhost',
    '127.0.0.1',
    'localhost:5173',
    'localhost:3000',
    'localhost:8000',
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",   # React default
    "http://localhost:8000",   # Django dev server
    "http://localhost:5173",   # Vite default
    "http://127.0.0.1:5173"    # Vite on 127.0.0.1
]