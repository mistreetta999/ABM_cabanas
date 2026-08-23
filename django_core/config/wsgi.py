"""
WSGI config para el proyecto Django.

Este archivo expone la aplicación WSGI como una variable llamada `application`.
Se utiliza para desplegar el proyecto en servidores compatibles con WSGI.
"""

import os
from django.core.wsgi import get_wsgi_application

# Ajusta el nombre del módulo de settings a tu proyecto real
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_project.settings")

application = get_wsgi_application()
