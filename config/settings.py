"""Archivo de configuración principal de Django"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # carga el archivo .env en la raíz del proyecto

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"


# pylint: disable=invalid-name
BASE_DIR = Path(__file__).resolve().parent
if BASE_DIR.name in ["settings", "cabanas_principal", "config"]:
    BASE_DIR = BASE_DIR.parent

# Cargar variables de entorno (.env)
if load_dotenv is not None:
    load_dotenv(BASE_DIR / ".env")

# Detector automático de carpetas
sys.path.append(str(BASE_DIR))
for root, dirs, files in os.walk(BASE_DIR):
    if any(part in root for part in ["venv", ".git", "__pycache__", "staticfiles", "media"]):
        continue
    if root not in sys.path:
        sys.path.append(root)

sys.path.append(str(BASE_DIR / "django_core" / "cabanas_apps_django"))

def config(name, default=None):
    """Obtiene una variable de entorno de forma segura."""
    value = os.getenv(name)
    return default if value is None else value

# Configuración de Seguridad
SECRET_KEY = config("SECRET_KEY", default="django-insecure-default-key")
DEBUG = str(config("DEBUG", "True")).lower() in ["true", "1", "yes"]

# ALLOWED_HOSTS siempre como lista
ALLOWED_HOSTS = config("ALLOWED_HOSTS", "*").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

# Settings visuales del Admin
ADMIN_SITE_HEADER = "Gestión de Cabañas"
ADMIN_SITE_TITLE = "Panel de Administración"
ADMIN_INDEX_TITLE = "Bienvenidos a cabanas"

# Modelo de usuario personalizado
#
# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "cabanas_principal",
    "cabanas_api",  
    # Terceros
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "django_extensions",

    # Mis aplicaciones
    "django_core.cabanas_apps_django.clientes",
    "django_core.cabanas_apps_django.reservas",
    "django_core.cabanas_apps_django.cabanas",
    "django_core.cabanas_apps_django.pagos",
    "django_core.cabanas_apps_django.web",
    "django_core.cabanas_apps_django.chatbot_app",
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
    "corsheaders.middleware.CorsMiddleware",
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


ROOT_URLCONF = "cabanas_principal.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "Templates"],
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

WSGI_APPLICATION = "cabanas_principal.wsgi.application"

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
            "NAME": BASE_DIR / "db.sqlite3",
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

# Archivos estáticos y multimedia
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
