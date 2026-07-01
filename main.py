""" este main para Django sin necesidad de usar la línea de comandos directamente.  """
import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
import subprocess
import webbrowser

def iniciar_servidor():
    subprocess.Popen(["python", "manage.py", "runserver"])
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    iniciar_servidor()


class DjangoAppRunner:
    """Class para ejecutar comandos de Django sin usar la línea de comandos directamente."""    
    def __init__(self, settings_module="cabanas_project.settings"):
        # Configura el módulo de settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
        self.application = get_wsgi_application()

    def runserver(self, host="127.0.0.1", port="8000"):
        """Arranca el servidor Django en host:port"""
        sys.argv = ["manage.py", "runserver", f"{host}:{port}"]
        execute_from_command_line(sys.argv)

    def migrate(self):
        """Ejecuta migraciones"""
        sys.argv = ["manage.py", "migrate"]
        execute_from_command_line(sys.argv)

    def createsuperuser(self):
        """Crea superusuario interactivo"""
        sys.argv = ["manage.py", "createsuperuser"]
        execute_from_command_line(sys.argv)


if __name__ == "__main__":
    # Inicializa con settings del proyecto
    runner = DjangoAppRunner()

    # Ejemplo: arranca servidor en localhost:8000
    runner.runserver()
