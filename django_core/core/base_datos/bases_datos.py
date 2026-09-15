"""Configuración central de bases de datos para el proyecto Django"""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

DJANGO_ENV = os.getenv("DJANGO_ENV", "development")


def get_database_config():
    """Devuelve la configuración de la base de datos según el entorno"""
    if DJANGO_ENV == "production":
        return {
            "default": {
                "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
                "NAME": os.getenv("DB_NAME", "api_db"),
                "USER": os.getenv("DB_USER", "carolina"),
                "PASSWORD": os.getenv("DB_PASSWORD", ""),
                "HOST": os.getenv("DB_HOST", "localhost"),
                "PORT": os.getenv("DB_PORT", "5432"),
            }
        }
    else:
        return {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }


# Exportar configuración
DATABASES = get_database_config()
