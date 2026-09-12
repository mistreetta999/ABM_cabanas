"""Archivo main.py."""
import os
import sys
import django
from django.core.exceptions import ImproperlyConfigured
from django.core.management import CommandError, execute_from_command_line

def main():
    """Punto de entrada principal para tu proyecto Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_project.settings")
    
    try:
        django.setup()
        execute_from_command_line(sys.argv)
    except (ImportError, ImproperlyConfigured, CommandError) as e:
        print(f"Error al iniciar el proyecto: {e}")

if __name__ == "__main__":
    main()
