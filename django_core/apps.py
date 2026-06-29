"""Configuracion de la aplicacion principal django_core."""

from django.apps import AppConfig


class DjangoCoreConfig(AppConfig):
    """ Configuracion de la aplicacion principal django_core."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_core"


class DjangoChatbotConfig(AppConfig):
    """ Config for the chatbot app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
class DjangoCabanasAppConfig(AppConfig):
    """ Config for the cabanas app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_app'
class DjangoAlquilerConfig(AppConfig):
    """ Config for the alquiler app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alquiler'
class DjangoReservaConfig(AppConfig):
    """ Config for the reserva app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reserva'
class DjangoClientesConfig(AppConfig):
    """ Config for the clientes app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'
class DjangoPagosConfig(AppConfig):
    """ Config for the pagos app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagos'
class DjangoRegistrosConfig(AppConfig):
    """ Config for the registros app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registros'
class DjangoGestionCabanasConfig(AppConfig):
        """ Config for the gestion cabanas app """
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'gestion'
class DjangoCabanasAppsConfig(AppConfig):
    """ Config for the cabanas_apps app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps'
class DjangoAdminConfig(AppConfig):
    """ Config for the admin app """
    default_auto_field = 'django.db.models.BigAutoField'
    clientes_admin = 'clientes_admin'
    pagos_admin = 'pagos_admin'
    registros_admin = 'registros_admin'
    gestion_admin = 'gestion_admin'
    cabanas_apps_admin = 'cabanas_apps_admin'
    name = 'admin'

        