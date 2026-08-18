"""
Módulo de configuración de base de datos para el proyecto de gestión de Cabanas.
Permite alternar entre SQLite3 (desarrollo) y PostgreSQL (producción).
"""

import os
from pathlib import Path
from django_core.conf.setting  import settings
from django_core.models import Models, Chatbot, CharField, Cabanas
 ,Cliente, Reserva, RegistroDiario, Factura, Pago, clean, save, __str__, __init__, __repr__, __eq__, __ne__, __hash__  

from django.db import connections, DEFAULT_DB_ALIAS

DATABASE_ROUTERS = ['cabanas_project.db.DatabaseRouter']
# django_core/db.py

class Database:
    """
    Clase para manejar la conexión a la base de datos.
    Compatible con la configuración de Django en settings.py.
    """

    def __init__(self, alias=DEFAULT_DB_ALIAS):
        self.alias = alias
        self.connection = connections[self.alias]

    def get_connection(self):
        """Devuelve la conexión activa"""
        return self.connection

    def cursor(self):
        """Devuelve un cursor para ejecutar SQL directo"""
        return self.connection.cursor()

    def close(self):
        """Cierra la conexión"""
        self.connection.close()

class DatabaseRouter:
    """Router para manejar múltiples bases de datos"""
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cabanas':
            return 'default'
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'cabanas':
            return 'default'
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'cabanas' or obj2._meta.app_label == 'cabanas':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'cabanas':
            return db == 'default'
        return None

# Configuración de la base de datos según entorno
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'gestion_cabanas'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'tu_password'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
class DatabaseConfig:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.DB_ENGINE = os.getenv("DB_ENGINE", "sqlite3")  # valores posibles: "sqlite3", "postgresql"

    def get_database_settings(self):
        """Devuelve la configuración de la base de datos según el motor seleccionado."""
        if self.DB_ENGINE == "postgresql":
            return {
                "default": {
                    "ENGINE": "django.db.backends.postgresql",
                    "NAME": os.getenv("POSTGRES_DB", "gestion_cabanas"),
                    "USER": os.getenv("POSTGRES_USER", "postgres"),
                    "PASSWORD": os.getenv("POSTGRES_PASSWORD", "tu_password"),
                    "HOST": os.getenv("POSTGRES_HOST", "localhost"),
                    "PORT": os.getenv("POSTGRES_PORT", "5432"),
                }
            }
        else:
            return {
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": self.BASE_DIR / "db.sqlite3",
                }
            }

BASE_DIR = Path(__file__).resolve().parent.parent

# Selección de motor de base de datos según variable de entorno
DB_ENGINE = os.getenv("DB_ENGINE", "sqlite3")  # valores posibles: "sqlite3", "postgresql"

if DB_ENGINE == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB", "gestion_cabanas"),
            "USER": os.getenv("POSTGRES_USER", "postgres"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "tu_password"),
            "HOST": os.getenv("POSTGRES_HOST", "localhost"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

db = Database()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM django_core_cabana;")
result = cursor.fetchone()
print("Cantidad de Cabanas:", result[0])
