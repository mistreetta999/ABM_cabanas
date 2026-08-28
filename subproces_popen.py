""" popen"""
import os
import subprocess
import webbrowser
import time

def iniciar_proyecto():
    """
    Levanta el servidor Django del proyecto 'cabanas'
    y abre el panel principal que conecta con todas las apps.
    """
    # Ruta al intérprete del entorno virtual
    venv_python = os.path.join(os.getcwd(), "..", "..", ".venv", "Scripts", "python.exe")

    # Ruta al manage.py en la raíz del proyecto
    manage_py = os.path.join(os.getcwd(), "..", "..", "manage.py")

    # Comando para levantar el servidor
    comando = [venv_python, manage_py, "runserver"]

    # Inicia el servidor en segundo plano desde la raíz del proyecto
    servidor = subprocess.Popen(comando, cwd=os.path.join(os.getcwd(), "..", ".."))

    # Espera unos segundos para que arranque
    time.sleep(3)

    # Abre navegador en el panel principal
    webbrowser.open("http://127.0.0.1:8000/")

    # Mantiene el servidor activo
    servidor.wait()

if __name__ == "__main__":
    iniciar_proyecto()
