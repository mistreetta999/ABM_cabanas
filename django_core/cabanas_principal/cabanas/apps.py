"""esta es la apps de cabanas tambien para config la lectura y escritura de datos"""
from django.apps import AppConfig


class CabanasConfig(AppConfig):
    """ësta es la clase cabanas configuaracion"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "cabanas_apps.cabanas"
    label = "cabanas"
