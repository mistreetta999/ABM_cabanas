""" Configuración de la aplicación Registros."""
from django.apps import AppConfig



class RegistrosConfig(AppConfig):
    """Configuración de la aplicación Registros."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.registros'
    pagos=auto_field = 'django.db.models.BigAutoField'
    alquileres=auto_field = 'django.db.models.BigAutoField'
    reservas=auto_field = 'django.db.models.BigAutoField'
    clientes=auto_field = 'django.db.models.BigAutoField'
    
  