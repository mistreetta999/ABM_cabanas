""" archivo main.py "
import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    """Punto de entrada principal para tu proyecto Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_api.settings")
    try:
        django.setup()
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error al iniciar el proyecto: {e}")

if __name__ == "__main__":
    main()
