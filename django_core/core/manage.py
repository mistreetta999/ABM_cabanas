#!/usr/bin/env python
"""
manage.py
Punto de entrada para ejecutar comandos de Django.
"""

import os
import sys
from django.core.management import execute_from_command_line


def manage():
    """Ejecuta tareas administrativas de Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_project.settings")
    try:
        execute_from_command_line(sys.argv)
    except Exception as exc:
        raise RuntimeError(
            f"Error al ejecutar comandos de Django: {exc}"
        ) from exc


if __name__ == "__main__":
    manage()
