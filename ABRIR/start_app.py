"""star apps"""

import os
import subprocess
import time
import webbrowser


def iniciar_servidor():
    """iniciar el servido"""
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")

    # Levantar servidor Django
    server = subprocess.Popen([venv_python, "manage.py", "runserver"])

    # Esperar unos segundos para que arranque
    time.sleep(3)

    # Abrir navegador en la página principal
    webbrowser.open("http://127.0.0.1:8000/")

    # Mantener el servidor corriendo
    server.wait()


if __name__ == "__main__":
    iniciar_servidor()
