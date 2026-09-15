"""Archivo de configuración principal de Django"""

import os
import sys
from pathlib import Path

from django.apps import AppConfig
from dotenv import load_dotenv


class WebConfig(AppConfig):
    """web app configuration"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_core.cabanas_apps_django.web"


# Cargar variables de entorno
load_dotenv()


def config(name, default=None):
    """Obtiene una variable de entorno de forma segura."""
    value = os.getenv(name)
    return default if value is None else value


# Base del proyecto (en minúsculas, consistente)
base_dir = Path(__file__).resolve().parent.parent

# Ajustar sys.path para que Django encuentre las apps
sys.path.append(str(base_dir))
sys.path.append(str(base_dir / "django_core" / "cabanas_apps_django"))

# Seguridad
SECRET_KEY = config("SECRET_KEY", default="django-insecure-default-key")
DEBUG = str(config("DEBUG", "True")).lower() in ["true", "1", "yes"]

ALLOWED_HOSTS = config("ALLOWED_HOSTS", "*").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

# Admin visual
ADMIN_SITE_HEADER = "Gestión de Cabañas"
ADMIN_SITE_TITLE = "Panel de Administración"
ADMIN_INDEX_TITLE = "Bienvenidos a cabanas"

# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Terceros
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "django_extensions",
    "crispy_forms",
    "crispy_bootstrap5",
    # Mis aplicaciones reales
    "django_core.cabanas_apps_django.clientes",
    "django_core.cabanas_apps_django.reservas",
    "django_core.cabanas_apps_django.alquileres",
    "django_core.cabanas_apps_django.cabanas",
    "django_core.cabanas_apps_django.pagos",
    "django_core.cabanas_apps_django.facturas",
    "django_core.cabanas_apps_django.web",
    "django_core.cabanas_apps_django.chatbot_app",
    "django_core.cabanas_apps_django.registros",
]

# DRF + drf-spectacular
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
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configuración CORS
CORS_ALLOW_ALL_ORIGINS = True

# URLs y WSGI
ROOT_URLCONF = "django_core.core.urls"
WSGI_APPLICATION = "django_core.core.wsgi.application"

# Base de datos
DJANGO_ENV = config("DJANGO_ENV", "development")

if DJANGO_ENV == "production":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME", "cabanas_db"),
            "USER": config("DB_USER", "carolina"),
            "PASSWORD": config("DB_PASSWORD", "1234"),
            "HOST": config("DB_HOST", "localhost"),
            "PORT": config("DB_PORT", "5432"),
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": base_dir / "db.sqlite3",
        },
    }

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalización
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Cordoba"
USE_I18N = True
USE_TZ = True

# Archivos estáticos y multimedia
STATIC_URL = "/static/"
STATICFILES_DIRS = [base_dir / "static"]
STATIC_ROOT = base_dir / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = base_dir / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Bootstrap 5 para formularios
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [base_dir / "Templates"],
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
