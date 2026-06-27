"""
WSGI config para el núcleo del proyecto de gestión de Cabanas.

Este archivo expone la aplicación WSGI como un objeto llamado `application`.
Se utiliza para desplegar el proyecto en servidores compatibles con WSGI.
"""

import os
from django.core.wsgi import get_wsgi_application

# Configuración del módulo de settings global
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabanas_project.settings')

# Objeto WSGI que usará el servidor
application = get_wsgi_application()
