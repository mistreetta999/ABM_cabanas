"""Configuracion de la aplicacion principal django_core."""

from django.apps import AppConfig


class DjangoCoreConfig(AppConfig):
    """ Configuracion de la aplicacion principal django_core."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_core"
