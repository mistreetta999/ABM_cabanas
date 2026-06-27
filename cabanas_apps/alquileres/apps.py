"""Configuración de la aplicación de reservas y alquileres."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.module_loading import autodiscover_modules

class ReservasAlquileresAppsConfig(AppConfig):
    """ class ReservasAlquileresAppsConfig representa la configuración de la aplicación de reservas y alquileres.""""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.reservas_alquileres_apps'
class AlquileresAppsConfig(AppConfig):
    """ class AlquileresAppsConfig representa la configuración de la aplicación de alquileres.""""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.alquileres_apps'
class RegistrosAppsConfig(AppConfig):
    """ class RegistrosAppsConfig representa la configuración de la aplicación de registros.""""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.registros_apps'
    
