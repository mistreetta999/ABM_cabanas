""""handels"""
import os

import subprocess
import webbrowser
import time

def abrir_cabanas():
    # Ruta al intérprete de tu entorno virtual
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")

    # Comando para levantar el servidor Django
    comando = [venv_python, "manage.py", "runserver"]

    # Inicia el servidor
    servidor = subprocess.Popen(comando)

    # Espera unos segundos para que arranque
    time.sleep(3)

    # Abre la página principal automáticamente
    webbrowser.open("http://127.0.0.1:8000/")

    # Mantiene el servidor activo
    servidor.wait()

if __name__ == "__main__":
    abrir_cabanas()
