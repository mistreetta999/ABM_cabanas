"""Configuracion de la app gestion_cabanas."""
from django.apps import AppConfig


class GestionCabanasConfig(AppConfig):
    """Configuracion de la app gestion_cabanas."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "cabanas_apps.gestion_cabanas"
    label = "gestion_cabanas"
    interfaz_app_label = "interfaz_gestion_cabanas"
    interfaz_app_name = "cabanas_apps.interfaz_gestion_cabanas"

    def get_interfaz_config(self):
        """Devuelve el AppConfig relacionado de interfaz_gestion_cabanas."""
        from django.apps import apps

        return apps.get_app_config(self.interfaz_app_label)
