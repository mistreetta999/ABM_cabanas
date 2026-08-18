"""
ASGI config para la aplicación cabanas_apps.
Este archivo expone la aplicación ASGI como una variable llamada `application`.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas.settings")

application = get_asgi_application()
