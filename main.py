import os
import sys

import django
from django.core.management import execute_from_command_line


class Management:
    def __init__(self, settings_module: str = "cabanas_project.settings"):
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        self.settings_module = settings_module
        os.environ["DJANGO_SETTINGS_MODULE"] = self.settings_module
        self.project_name = "Sistema de Gestion de Cabanas"

    def inicializar_django(self):
        django.setup()
        print(f"--- {self.project_name} inicializado con exito ---")

    def ejecutar_comando(self):
        if len(sys.argv) == 1:
            sys.argv.extend(["runserver", "127.0.0.1:8000"])
        execute_from_command_line(sys.argv)


def main():
    app = Management()
    app.inicializar_django()
    app.ejecutar_comando()


if __name__ == "__main__":
    main()
