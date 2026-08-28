"""WSGI para interfaz_gestion_cabanas."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings")

application = get_wsgi_application()
