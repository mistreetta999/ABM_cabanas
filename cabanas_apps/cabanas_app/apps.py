from django.apps import AppConfig
from django_core.db import Database

def ejemplo_consulta():
    db = Database()
    resultados = db.execute("SELECT * FROM cabanas_cabana")
    return resultados

class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_app.clientes'
