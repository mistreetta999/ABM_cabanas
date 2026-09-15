"""cli"""

import os
import subprocess
import sys
import webbrowser

BASE_DIR = r"C:\Users\carol\OneDrive\Desktop\cabanas"
VENV_PYTHON = os.path.join(BASE_DIR, ".venv", "Scripts", "python.exe")
MANAGE_PY = os.path.join(BASE_DIR, "manage.py")


def runserver():
    """Levanta el servidor Django y abre la página principal."""
    comando = [VENV_PYTHON, MANAGE_PY, "runserver"]
    subprocess.Popen(comando, cwd=BASE_DIR)
    webbrowser.open("http://127.0.0.1:8000/")


def makemigrations(app=None):
    """Crea migraciones (global o por app)."""
    comando = [VENV_PYTHON, MANAGE_PY, "makemigrations"]
    if app:
        comando.append(app)
    subprocess.call(comando, cwd=BASE_DIR)


def migrate():
    """Aplica migraciones."""
    subprocess.call([VENV_PYTHON, MANAGE_PY, "migrate"], cwd=BASE_DIR)


def shell():
    """Abre shell interactiva de Django."""
    subprocess.call([VENV_PYTHON, MANAGE_PY, "shell"], cwd=BASE_DIR)


def main():
    if len(sys.argv) < 2:
        print("Uso: python cli.py [runserver|makemigrations|migrate|shell]")
        return

    comando = sys.argv[1]

    if comando == "runserver":
        runserver()
    elif comando == "makemigrations":
        app = sys.argv[2] if len(sys.argv) > 2 else None
        makemigrations(app)
    elif comando == "migrate":
        migrate()
    elif comando == "shell":
        shell()
    else:
        print(f"Comando desconocido: {comando}")


if __name__ == "__main__":
    main()
