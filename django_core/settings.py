""" configutacion paratodos los archivos"""
import os

from pathlib import Path
from DATABASE.Database import get_database_settings
BASE_DIR = Path(__file__).resolve().parent.parent


class SettingsCabana:
    """
    Configuración principal del proyecto de gestión de Cabanas.
    """

    # Seguridad
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-secreta-desarrollo")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

    # Aplicaciones instaladas
    INSTALLED_APPS = [
        
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "cabana_app",              # tu app principal
        "cabana_app.clientes",     # módulo clientes
        "cabana_app.alquileres_reservas",  # módulo alquileres y reservas
        "chatbot", 
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # módulo chatbot
        "cabanas_project.cabanas",  # módulo Cabanas
         # apps
         "rest_framework",
        "django_filters",
        "drf_yasg",
        "corsheaders",
        "django_extensions",
        "django_core",
        
        
        "cabanas",
        "cabanas_apps.reservas",
        "cabana_project.reservas",
        "cabanas_apps.clientes",
        "cabanas_apps.registros",
        "DATABASE",
        "Template",
         "django.contrib.messages",
        "django.contrib.staticfiles",
        "formularios",
            "Chatbot",
            "Chatbot.models",
            "Chatbot.views",
            "Chatbot.urls",
            "Chatbot.apps",
            "Chatbot.signals",
            "Chatbot.admin",
        ""
    ]

    # Middleware
    MIDDLEWARE = [
        "django.middle ware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware", 
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    ]

    ROOT_URLCONF = "django_core.urls"

    # Templates
    TEMPLATES = [

        
        
        
    ]

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

    ROOT_URLCONF = "django_core.urls"

    # Templates
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
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

    WSGI_APPLICATION = "django_core.wsgi.application"

    # Base de datos (SQLite o PostgreSQL según entorno)
    DATABASES = get_database_settings()

    # Autenticación
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

    # Archivos estáticos
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [BASE_DIR / "static"]

    # Archivos multimedia
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_tu_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
