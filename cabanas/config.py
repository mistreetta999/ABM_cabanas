""" config cabanas"""
import os
import subprocess
import webbrowser
from django.apps import AppConfig


class IniciarDjangoConfig(AppConfig):
    """Configuración de la aplicación para iniciar Django."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas.config'

    def iniciar_django(self):
        """Inicia el servidor Django y abre el navegador en la URL local."""
        # Aseguramos que estamos en la carpeta del proyecto
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Levanta el servidor Django
        subprocess.Popen(["python", "manage.py", "runserver"])

        # Abre el navegador en la URL local
        webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    config = IniciarDjangoConfig("cabanas.config", None)
    config.iniciar_django()


class CabanasConfig(AppConfig):
    """Configuración de la aplicación Cabañas."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas'


class AlquileresConfig(AppConfig):
    """Configuración de la aplicación Alquileres."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.alquileres'


class ClientesConfig(AppConfig):
    """Configuración de la aplicación Clientes."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.clientes'


class PagosConfig(AppConfig):
    """Configuración de la aplicación Pagos."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.pagos'


class ReservasConfig(AppConfig):
    """Configuración de la aplicación Reservas."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.reservas'


class ChatbotAppConfig(AppConfig):
    """Configuración de la aplicación Chatbot."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.chatbot_app'


class CabanasApiConfig(AppConfig):
    """Configuración de la aplicación Cabañas API."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_api'


class CabanasWebConfig(AppConfig):
    """Configuración de la aplicación Cabañas Web."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_web'


class CabanasAdminConfig(AppConfig):
    """Configuración de la aplicación Cabañas Admin."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_admin'


class ViewsCabanasConfig(AppConfig):
    """Configuración de la aplicación Views Cabañas."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.views_cabanas'


class CabanasModelsConfig(AppConfig):
    """Configuración de la aplicación Cabañas Models."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_models'


class CabanasFormsConfig(AppConfig):
    """Configuración de la aplicación Cabañas Forms."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_forms'


class CabanasTemplatesConfig(AppConfig):
    """Configuración de la aplicación Cabañas Templates."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.cabanas_templates'


class ProyectoConfig(AppConfig):
    """Configuración de la aplicación Proyecto."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cabanas_apps.proyecto'
