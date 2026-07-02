"""App configuracion   para cabanas_apps """ 
from django.apps import AppConfig
from cabanas_apps.reservas import handlers as reservas
from cabanas_apps.reservas import views as reservas

class CabanaAppsConfig(AppConfig):
    """App configuracion para cabanas_apps."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.gestion_cabanas'
class InterfazGestionCabanasConfig(AppConfig):
    """App configuracion para interfaz_gestion_cabanas."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.interfaz_gestion_cabanas'
