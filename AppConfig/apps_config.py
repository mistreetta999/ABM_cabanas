"""Configuración de la aplicación AppConfig."""

from django.apps import AppConfig


class AppConfigApp(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "AppConfig"
    verbose_name = "Configuración del Sistema"
