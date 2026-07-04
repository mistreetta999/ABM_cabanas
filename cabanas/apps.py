""""Este archivo se encarga de iniciar el servidor Django y abrir el navegador en la URL local.
"""
import os
import subprocess
import webbrowser
from django.apps import AppConfig
from django.core.management import execute_from_command_line
from django import forms
from .models import Cabana
from django.http import HttpResponse,HttpRequest

def home_view(request: HttpRequest) -> HttpResponse:
    """"Vista para la página principal completa.
    """


    return HttpResponse("")  # Página principal vacía

def iniciar_django():
    """Inicia el servidor Django y abre el navegador en la URL local."""
    # Aseguramos que estamos en la carpeta del proyecto
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Levanta el servidor Django
    subprocess.Popen(["python", "manage.py", "runserver"])
    
    # Abre el navegador en la URL local
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    iniciar_django()
