"""Archivo de configuración auxiliar para el proyecto Django."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar archivo .env si existe
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def get_env_variable(name: str, default: str = None) -> str:
    """
    Obtiene una variable de entorno.
    Si no existe, devuelve el valor por defecto.
    """
    return os.getenv(name, default)

# Configuración básica
SECRET_KEY = get_env_variable("SECRET_KEY", "django-insecure-default-key")
DEBUG = get_env_variable("DEBUG", "False").lower() in ("true", "1")

# Configuración de base de datos
DB_NAME = get_env_variable("DB_NAME", "cabanas_db")
DB_USER = get_env_variable("DB_USER", "Aministrador")
DB_PASSWORD = get_env_variable("DB_PASSWORD", "")
DB_HOST = get_env_variable("DB_HOST", "localhost")
DB_PORT = get_env_variable("DB_PORT", "5432")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

# Configuración de rutas estáticas y media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Idioma y zona horaria
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Cordoba"
USE_I18N = True
USE_TZ = True
