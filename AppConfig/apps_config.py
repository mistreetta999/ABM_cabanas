"""Configuraciones auxiliares de apps del proyecto."""
from django.apps import AppConfig

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

class AppsConfig(AppConfig):
    """Config de la app apps."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "apps.apps"
    label = "apps"

class CabanasConfig(AppConfig):
    """Config de la app cabanas."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.cabanas"
    label = "cabanas"

class ReservasConfig(AppConfig):
    """Config de la app reservas."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.reservas"
    label = "reservas"

class AlquileresConfig(AppConfig):
    """Config de la app alquileres."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.alquileres"
    label = "alquileres"

class ClientesConfig(AppConfig):
    """Config de la app clientes."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.clientes"
    label = "clientes"

class PagosConfig(AppConfig):
    """Config de la app pagos."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.pagos"
    label = "pagos"

class RegistrosConfig(AppConfig):
    """Config de la app registros."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.registros"
    label = "registros"

class GestionCabanasConfig(AppConfig):
    """Config de la app gestion_cabanas."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.gestion_cabanas"
    label = "gestion_cabanas"

class InterfazGestionCabanasConfig(AppConfig):
    """Config de la app interfaz_gestion_cabanas."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.interfaz_gestion_cabanas"
    label = "interfaz_gestion_cabanas"

class ViewsInterfazCabanasConfig(AppConfig):
    """Config de la app views_interfaz_cabanas."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.views_interfaz_cabanas"
    label = "views_interfaz_cabanas"

class HandlesInterfazCabanasConfig(AppConfig):
    """Config de la app handles_interfaz_cabanas."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_apps.handles_interfaz_cabanas"
    label = "handles_interfaz_cabanas"

class ApiConfig(AppConfig):
    """Config de la app cabanas_api."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "cabanas_api"
    label = "cabanas_api"

class DataBaseConfig(AppConfig):
    """Config de la app cabanas_database."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "DATABASE"
    label = "DATABASE"

class ChatbotConfig(AppConfig):
    """Config de la app cabanas_chatbot."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "chatbot_app"
    label = "chatbot_app"

class TemplateConfig(AppConfig):
    """Config de la app Template."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "Template"
    label = "Template"

class PaginaPrincipalConfig(AppConfig):
    """Config de la app pagina_principal."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "pagina_principal"
    label = "pagina_principal"

class ApiAppConfig(AppConfig):
    """Config de la app api."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "api"
    label = "api"

class RenderConfig(AppConfig):
    """Config de la app render."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "render"
    label = "render"

class DjangoCoreConfig(AppConfig):
    """Config de la app django_core."""
    default_auto_field = DEFAULT_AUTO_FIELD
    name = "django_core"
    