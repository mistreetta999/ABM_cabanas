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
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")

    # Comando para levantar el servidor
    comando = [venv_python, "manage.py", "runserver"]

    # Inicia el servidor en segundo plano
    servidor = subprocess.Popen(comando)

    # Espera unos segundos para que arranque
    time.sleep(3)

    # Abre navegador en el panel principal
    webbrowser.open("http://127.0.0.1:8000/")

    # Mantiene el servidor activo
    servidor.wait()

if __name__ == "__main__":
    iniciar_proyecto()
