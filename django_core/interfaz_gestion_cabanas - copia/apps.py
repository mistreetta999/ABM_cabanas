""""Este archivo se encarga de iniciar el servidor Django y abrir el navegador en la URL local.
"""
import os
import subprocess
import webbrowser
from django.apps import AppConfig
from django.core.management import execute_from_command_line
def iniciar_django():
    # Aseguramos que estamos en la carpeta del proyecto
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Levanta el servidor Django
    subprocess.Popen(["python", "manage.py", "runserver"])
    
    # Abre el navegador en la URL local
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    iniciar_django()
