"""
Este módulo configura las aplicaciones Django para el proyecto de gestión de Cabanas.
Las clases definidas aquí permiten configurar y gestionar las aplicaciones del proyecto.
"""
from typing import Any, Dict #importacion de tipos

import os # necesito importar os
import sys
import django
from django.core.management import execute_from_command_line
from django.core.management.base import CommandError
from django.core.exceptions import ImproperlyConfigured



class Apps:
    """Configuración de aplicaciones para el proyecto Cabanas."""
    def __init__(self):
        self.apps: Dict[str, Any] = {}
        self.debug: bool = True
        self.installed_apps: list = []
        self.middleware: list = []
        self.databases: Dict[str, Any] = {}
        self.Templates: Dict[str, Any] = {}
        self.static_files: Dict[str,Any] = {}
        self.i18n: Dict[str, Any] = {}
        self.security: Dict[str, Any] = {}
        self.logging: Dict[str, Any] = {}
        self.email: Dict[str, Any] = {}
        self.cache: Dict[str, Any] = {}
        self.authentication: Dict[str, Any] = {}
class Managment:
    """
    Clase principal para inicializar y ejecutar comandos Django
    en el proyecto de gestión de Cabanas.
    """

    def __init__(self, settings_module: str = "cabanas_project.settings"):
        """
        Inicializa la configuración del proyecto.

        Args:
            settings_module (str): Ruta al módulo de configuración de Django.
        """
        self.settings_module = settings_module
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", self.settings_module)
        self.project_name = "Sistema de Gestión de Cabanas"

    def inicializar_django(self):
        """
        Inicializa Django y muestra un mensaje de éxito.
        Maneja errores de configuración o instalación.
        """
        try:
            django.setup()
            print(f"--- {self.project_name} inicializado con éxito ---")
        except ImportError:
            print("Error: Django no está instalado en el entorno actual.")
            sys.exit(1)
        except ImproperlyConfigured as exc:
            print(f"Error de configuración en Django: {exc}")
            sys.exit(1)

    def ejecutar_comando(self):
        """
        Ejecuta cualquier comando de Django (runserver, migrate, etc.).
        Maneja errores de ejecución de comandos.
        """
        try:
            execute_from_command_line(sys.argv)
        except CommandError as exc:
            print(f"Error al ejecutar comando: {exc}")
            sys.exit(1)



if __name__ == "__main__":

    print("Configuración de aplicaciones para el proyecto Cabanas.")
    print("Este módulo configura las aplicaciones Django para el proyecto de gestión de Cabanas.")
    print("Las clases definidas aquí permiten configurar y gestionar las aplicaciones del proyecto.")
