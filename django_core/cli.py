"""CLI para iniciar el proyecto Django desde un archivo alternativo."""

import os
import sys
from django.core.management import execute_from_command_line

def main():
    # Configuración del módulo de settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings")

    try:
        execute_from_command_line(sys.argv)
    except Exception as exc:
        raise RuntimeError("Error al iniciar el proyecto Django") from exc

if __name__ == "__main__":
    main()
