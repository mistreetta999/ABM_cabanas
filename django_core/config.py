# django_core/config.py

import os
from pathlib import Path
# django_core/config.py
from pathlib import Path
from django_core.config import Settings   # Importamos la clase Settings
from pydantic import BaseSettings, Field
from pydantic_settings import SettingsConfigDict
from django_core.config import Settings

class Config(BaseSettings):
    """
    Clase de configuración del proyecto Django.
    Carga variables desde el archivo .env y define valores por defecto.
    """

    # Configuración básica
    SECRET_KEY: str = Field(..., description="Clave secreta de Django")
    DEBUG: bool = Field(default=True, description="Modo debug")
    ALLOWED_HOSTS: list[str] = Field(default=["*"], description="Hosts permitidos")

    # Configuración de base de datos
    DATABASE_URL: str = Field(..., description="URL de la base de datos")

    # Configuración de idioma y zona horaria
    LANGUAGE_CODE: str = Field(default="es-ar")
    TIME_ZONE: str = Field(default="America/Argentina/Cordoba")

    # Configuración de archivos estáticos
    STATIC_URL: str = Field(default="/static/")

    # Configuración de Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",        # archivo de variables de entorno
        env_file_encoding="utf-8",
        extra="ignore"          # ignora variables no declaradas
    )

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de la base de datos (ejemplo con SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Configuración de seguridad básica
SECRET_KEY = 'cambia-esta-clave-por-una-segura'
 DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# settings.py



# Instanciamos la configuración
settings = Settings()

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = settings.SECRET_KEY
DEBUG = settings.DEBUG
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Base de datos
DATABASES = settings.DATABASES

# Internacionalización
LANGUAGE_CODE = settings.LANGUAGE_CODE
TIME_ZONE = settings.TIME_ZONE
USE_I18N = settings.USE_I18N
USE_TZ = settings.USE_TZ

# Archivos estáticos
STATIC_URL = settings.STATIC_URL
STATICFILES_DIRS = settings.STATICFILES_DIRS

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tus apps personalizadas
    'cabanas_api
p',
    'clientes',
    'reservas',
    'alquileres',
]
