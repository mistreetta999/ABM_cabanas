"""
Configuración WSGI para el proyecto Cabanas.

Expone el invocable WSGI como una variable de nivel de módulo llamada ``application``.

Para más información sobre este archivo, vea:
https://djangoproject.com
"""

import os

from django.core.wsgi import get_wsgi_application

# Establece el módulo de configuración por defecto para la herramienta 'django-admin'.
# Se asume que el archivo de configuración está en cabana_app/settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabana_app.settings')

application = get_wsgi_application()

"""
Atributos:
    application (WSGIHandler): El punto de entrada para servidores web 
    compatibles con WSGI (como Gunicorn o mod_wsgi) para servir tu proyecto.
"""
