"""Archivo de configuración principal de Django"""
import os
from pathlib import Path
from dotenv import load_dotenv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_project.settings")
django.setup()

# Cargar variables de entorno desde .env
load_dotenv()

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY must be set as an environment variable")
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'cabanas-app.com']


AUTH_USER_MODEL = "cabanas_apps.clientes.UsuarioSistema"

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
    "cabanas_apps.cabanas",
    "cabanas_apps.clientes",
    "cabanas_apps.alquileres",
    "cabanas_apps.facturas",
    "cabanas_apps.usuarios",
    "cabanas_apps.reservas",
    "cabanas_apps.registros",
    "cabanas_apps.interfaz_gestion_cabanas",
    "cabanas_apps.gestion_cabanas",
    "cabanas_apps.chatbot_app",
    "web",

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

# Bases de datos: PostgreSQL (default) + SQL Server (secundaria)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    },
    "sqlserver": {
        "ENGINE": "mssql",
        "NAME": os.getenv("SQLSERVER_NAME"),
        "USER": os.getenv("SQLSERVER_USER"),
        "PASSWORD": os.getenv("SQLSERVER_PASSWORD"),
        "HOST": os.getenv("SQLSERVER_HOST"),
        "PORT": os.getenv("SQLSERVER_PORT"),
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    },
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

# Internacionalización
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Cordoba"
USE_I18N = True
USE_TZ = True

# Configuración por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
