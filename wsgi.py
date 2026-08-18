"""
WSGI config for cabanas project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

# Configura el módulo de settings de tu proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings.settings")

application = get_wsgi_application()
