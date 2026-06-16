#!/usr/bin/env python
from core.core import Management
import sys

class DjangoLauncher:
    """
    Clase principal en manage.py que inicializa el proceso.
    """
    def __init__(self):
        # Instanciamos la clase Management definida en core.py
        self.manager = Management(settings_path="cabanas_project.settings")

    def run(self):
        # 1. Definimos y configuramos el entorno
        self.manager.setup_environment()
        # 2. Ejecutamos los argumentos recibidos por consola (sys.argv)
        self.manager.execute(sys.argv)

if __name__ == "__main__":
    launcher = DjangoLauncher()
    launcher.run()