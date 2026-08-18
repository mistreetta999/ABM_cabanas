"""Archivo de configuración principal de Django"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

#  RUTA BASE DEL PROYECTO: AUTOMÁTICA, NO DEPENDE DE ONEDRIVE
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    # Django apps por defecto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias
    'cabanas_apps.gestion_cabanas',
    'cabanas_apps.chatbot_app',
    'cabanas_apps.reservas',
    'cabanas_apps.cabanas',
    'cabanas_apps.alquileres',
    'cabanas_apps.clientes',
    'cabanas_apps.pagos',
    'cabanas_apps.registros',

    # Django REST Framework
    'rest_framework',
    'drf_spectacular',

    # Extensiones
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_cabanas.urls'

Templates = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "Templates"],  # Ruta relativa
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

WSGI_APPLICATION = 'gestion_cabanas.wsgi.application'

# BASE DE DATOS: RUTA RELATIVA, NO FIJA A ONEDRIVE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator'
    },
]

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_TZ = True

# 📁 ARCHIVOS ESTÁTICOS Y MEDIA: RUTAS RELATIVAS
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración DRF
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Gestión de Cabañas API',
    'DESCRIPTION': 'Documentación de la API para reservas y gestión',
    'VERSION': '1.0.0',
}
