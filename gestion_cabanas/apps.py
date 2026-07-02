"""App configuracion   para cabanas_apps """ 
from django.apps import AppConfig

class CabanaAppsConfig(AppConfig):
    """App configuracion para cabanas_apps."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.gestion_cabanas'
class InterfazGestionCabanasConfig(AppConfig):
    """App configuracion para interfaz_gestion_cabanas."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.interfaz_gestion_cabanas'
