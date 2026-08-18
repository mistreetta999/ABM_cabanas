""" setting mediador"""
import os
import warnings

try:
    from importlib import import_module

    _settings_module = import_module("cabanas_principal.settings")
    globals().update(
        {
            name: value
            for name, value in vars(_settings_module).items()
            if not name.startswith("__")
        }
    )
except ImportError as e:
    warnings.warn(f"Error cargando settings originales: {e}")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = os.getenv("SECRET_KEY", "dummy-secret-key")
    DEBUG = True
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "cabanas_principal.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
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

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    LANGUAGE_CODE = "es-ar"
    TIME_ZONE = "America/Argentina/Cordoba"
    USE_I18N = True
    USE_TZ = True

    STATIC_URL = "/static/"
