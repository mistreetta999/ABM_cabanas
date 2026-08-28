import os
import subprocess
import webbrowser
import time

def abrir_django():
    # Ruta absoluta al manage.py
    proyecto_raiz = r"C:\Users\carol\OneDrive\Desktop\cabanas"
    manage_py = os.path.join(proyecto_raiz, "manage.py")

    # Ruta al Python del entorno virtual
    venv_python = os.path.join(proyecto_raiz, ".venv", "Scripts", "python.exe")

    # Comando para levantar el servidor
    comando = [venv_python, manage_py, "runserver"]

    # Ejecutar en la raíz del proyecto
    servidor = subprocess.Popen(comando, cwd=proyecto_raiz)

    # Esperar unos segundos para que arranque
    time.sleep(3)

    # Abrir navegador en la página principal (no admin)
    webbrowser.open("http://127.0.0.1:8000/")

    # Mantener el servidor activo
    servidor.wait()

if __name__ == "__main__":
    abrir_django()
