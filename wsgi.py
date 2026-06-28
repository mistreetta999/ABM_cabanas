"""
WSGI config for cabanas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Asegúrate de que el nombre del módulo de settings coincida con tu proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabanas.settings')

application = get_wsgi_application()
