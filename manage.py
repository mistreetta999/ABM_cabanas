"""Archivo de gestión principal de Django para el proyecto de cabañas."""

import os
import sys

def main():
    """Ejecuta las tareas administrativas de Django."""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings")

    try:
        # Intentar importar Django y manejar el caso en que no esté instalado
        from django.core.management import execute_from_command_line  # pylint: disable=import-outside-toplevel
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado en tu entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
