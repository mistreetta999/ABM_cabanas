"""
ASGI config for cabanas_principal project.

Expone la aplicación ASGI como una variable llamada `application`.
"""

import os

from django.core.asgi import get_asgi_application

# Apuntar al settings correcto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings")

application = get_asgi_application()
