""" apps de cabanas"""
from django.apps import AppConfig


class ChatbotConfig(AppConfig):
    """ Config for the chatbot app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
class CabanasAppConfig(AppConfig):
    """ Config for the cabanas app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_app'
class AlquilerConfig(AppConfig):
    """ Config for the alquiler app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alquiler'
class ReservaConfig(AppConfig):
    """ Config for the reserva app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reserva'
class ClientesConfig(AppConfig):
    """ Config for the clientes app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'
class PagosConfig(AppConfig):
    """ Config for the pagos app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagos'
class RegistrosConfig(AppConfig):
    """ Config for the registros app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registros'
class GestionConfig(AppConfig):
        """ Config for the gestion app """
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'gestion'
class CabanasAppsConfig(AppConfig):
    """ Config for the cabanas_apps app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps'
class AdminConfig(AppConfig):
    """ Config for the admin app """
    default_auto_field = 'django.db.models.BigAutoField'
    clientes_admin = 'clientes_admin'
    pagos_admin = 'pagos_admin'
    registros_admin = 'registros_admin'
    gestion_admin = 'gestion_admin'
    cabanas_apps_admin = 'cabanas_apps_admin'
    name = 'admin'

        