from . import viewsSTATIC_URL = "/static/"
from django_core import viewsSTATIC_URL = "/static/"
from django.urls import path, includeSTATIC_URL = "/static/"
from django.contrib import adminSTATIC_URL = "/static/"
""" archivo urls cabanas"""STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'

urlpatterns = [STATIC_URL = "/static/"
               STATICFILES_DIRS= [BASE_DIR / "static"]

               MEDIA_URL= "/media/"
               MEDIA_ROOT= BASE_DIR / "media"

               # WSGI
               WSGI_APPLICATION= 'cabanas.wsgi.application'

               path("admin/", admin.site.urls), STATIC_URL = "/static/"
               STATICFILES_DIRS = [BASE_DIR / "static"]

               MEDIA_URL = "/media/"
               MEDIA_ROOT = BASE_DIR / "media"

               # WSGI
               WSGI_APPLICATION = 'cabanas.wsgi.application'

               path("pagina_principal/", views.pagina_principal, name="pagina_principal"), STATIC_URL = "/static/"
               STATICFILES_DIRS = [BASE_DIR / "static"]

               MEDIA_URL = "/media/"
               MEDIA_ROOT = BASE_DIR / "media"

               # WSGI
               WSGI_APPLICATION = 'cabanas.wsgi.application'

               path("gestion/", views.gestion, name="gestion"), STATIC_URL = "/static/"
               STATICFILES_DIRS = [BASE_DIR / "static"]

               MEDIA_URL = "/media/"
               MEDIA_ROOT = BASE_DIR / "media"

               # WSGI
               WSGI_APPLICATION = 'cabanas.wsgi.application'

               path("chatbot/", include("chatbot.urls", namespace="chatbot")), STATIC_URL = "/static/"
               STATICFILES_DIRS = [BASE_DIR / "static"]

               MEDIA_URL = "/media/"
               MEDIA_ROOT = BASE_DIR / "media"

               # WSGI
               WSGI_APPLICATION = 'cabanas.wsgi.application'

               ]STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WSGI
WSGI_APPLICATION = 'cabanas.wsgi.application'
