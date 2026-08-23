"""
WSGI config para la aplicación cabanas_apps.
Este archivo expone la aplicación WSGI como una variable llamada `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas.settings")

application = get_wsgi_application()
