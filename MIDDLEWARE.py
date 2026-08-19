import os
import warnings

try:
    # Intentar cargar tu configuración principal
    from cabanas_principal.settings import *
except Exception as e:
    warnings.warn(f"Error cargando settings originales: {e}")

    # Configuración mínima de respaldo para que Django arranque
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

    AUTH_PASSWORD_VALIDATORS = []

    LANGUAGE_CODE = "es-ar"
    TIME_ZONE = "America/Argentina/Cordoba"
    USE_I18N = True
    USE_TZ = True

    STATIC_URL = "/static/"

class SafeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            from django.http import JsonResponse
            return JsonResponse({"error": str(e)}, status=500)
