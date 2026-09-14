"""Archivo de gestión principal de Django dentro del módulo core."""

import os
import sys


def main():
    """Ejecuta las tareas administrativas de Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_core.config.settings")
    try:
        # La importación diferida permite mostrar un mensaje claro si Django no está instalado.
        # pylint: disable=import-outside-toplevel
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado en tu entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
