#!/usr/bin/env python
"""
Archivo de utilidades de gestión para el proyecto.
"""
import sys
from django.core.management import execute_from_command_line
from django.core.management.base import CommandError


def main():
    """Ejecuta comandos de administración de Django."""
    try:
        execute_from_command_line(sys.argv)
    except CommandError as e:
        print(f"Error en el comando: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
