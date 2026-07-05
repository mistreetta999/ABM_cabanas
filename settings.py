"""Archivo de configuración principal de Django"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SILENCED_SYSTEM_CHECKS = ["*"]
# Aplicaciones instaladas
INSTALLED_APPS = [
    # Django apps por defecto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias
    "cabanas_apps.clientes",
    "cabanas_apps.reservas",
    "cabanas_apps.cabanas",
    "cabanas_apps.interfaz_gestion_cabanas",
    "cabanas_apps.chatbot",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
 
    # Django REST Framework y drf-spectacular
    'rest_framework',
    'drf_spectacular',

    #  Extensiones útiles
    'django_extensions',
]

# Configuración de DRF + drf-spectacular
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Gestión de Cabañas API',
    'DESCRIPTION': 'Documentación de la API para reservas, clientes y cabañas',
    'VERSION': '1.0.0',
}

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs principales
ROOT_URLCONF = 'cabanas.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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


STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

# Bases de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
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

# Internacionalización
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_TZ = True

# Configuración por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
