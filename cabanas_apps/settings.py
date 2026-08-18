"""Archivo de configuración principal de Django"""
import os
from pathlib import Path
from dotenv import load_dotenv
AUTH_USER_MODEL = "usuarios.Usuario"
# Cargar variables de entorno desde .env
load_dotenv()

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is required and must be set")
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'tuservidor.com']


# Aplicaciones instaladas
INSTALLED_APPS = [
    # Django apps por defecto
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps propias
    "cabanas_apps.cabanas_app",
    "cabanas_apps.cabanas",
    "cabanas_apps.usuarios",
    "cabanas_apps.clientes",
    "cabanas_apps.pagos",
    "cabanas_apps.alquileres",
    "cabanas_apps.reservas",
    "cabanas_apps.registros",
    "cabanas_apps.usuarios",
    "cabanas_apps.interfaz_gestion_cabanas",
    "cabanas_apps.gestion_cabanas",
    "cabanas_apps.chatbot_app",

    # Django REST Framework y drf-spectacular
    "rest_framework",
    "drf_spectacular",
    "corsheaders",

    # Extensiones útiles
    "django_extensions",
]

# Configuración de DRF + drf-spectacular
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Gestión de Cabañas API",
    "DESCRIPTION": "Documentación de la API para reservas, clientes y cabañas",
    "VERSION": "1.0.0",
}

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLs principales
ROOT_URLCONF = "cabanas_principal.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "Template"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Archivos estáticos y media
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = "cabanas_principal.wsgi.application"

# Bases de datos: SQLite3 local + PostgreSQL opcional
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "cabanas_db"),
        "USER": os.getenv("DB_USER", "carolina"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    },
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalización
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Cordoba"
USE_I18N = True
USE_TZ = True

# Configuración por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
