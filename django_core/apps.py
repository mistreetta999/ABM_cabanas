"""Configuracion de la aplicacion principal django_core."""

from django.apps import AppConfig
from typing import Any
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

def get_app_config(app_name):
    """ Devuelve la configuracion de la aplicacion especificada por su nombre. """
    app_configs = {
        'Chatbot': DjangoChatbotConfig,
        'cabanas_app': DjangoCabanasAppConfig,
        'alquiler': DjangoAlquilerConfig,
        'reserva': DjangoReservaConfig,
        'clientes': DjangoClientesConfig,
        'pagos': DjangoPagosConfig,
        'registros': DjangoRegistrosConfig,
        'gestion': DjangoGestionCabanasConfig,
        'cabanas_apps': DjangoCabanasAppsConfig,
        'interfaz_gestion_cabanas': DjangoAdminConfig
    }
    return app_configs.get(app_name, None)


class DjangoCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_core'

    def ready(self):
        from . import signals  # ejemplo correcto



class DjangoChatbotConfig(AppConfig):
    """ Config for the chatbot app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'Chatbot'

class DjangoCabanasAppConfig(AppConfig):
    """ Config for the cabanas app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'cabanas_app'

class DjangoAlquilerConfig(AppConfig):
    """ Config for the alquiler app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'alquiler'

class DjangoReservaConfig(AppConfig):
    """ Config for the reserva app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'reserva'

class DjangoClientesConfig(AppConfig):
    """ Config for the clientes app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'clientes'

class DjangoPagosConfig(AppConfig):
    """ Config for the pagos app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'pagos'

class DjangoRegistrosConfig(AppConfig):
    """ Config for the registros app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'registros'

class DjangoGestionCabanasConfig(AppConfig):
    """ Config for la gestion cabanas app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'gestion'

class DjangoCabanasAppsConfig(AppConfig):
    """ Config for the cabanas_apps app """
    default_auto_field = DEFAULT_AUTO_FIELD
    name = 'cabanas_apps'

class DjangoAdminConfig(AppConfig):
    """ Config for the interfaz_gestion_cabanas app """
    default_auto_field = DEFAULT_AUTO_FIELD
    clientes_admin = 'clientes_admin'
    pagos_admin = 'pagos_admin'
    registros_admin = 'registros_admin'
    gestion_admin = 'gestion_admin'
    cabanas_apps_admin = 'cabanas_apps_admin'
    name = 'interfaz_gestion_cabanas'

        
