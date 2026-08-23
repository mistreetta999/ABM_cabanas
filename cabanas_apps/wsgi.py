"""WSGI para cabanas_apps."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings.settings")

application = get_wsgi_application()
