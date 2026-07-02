""" archivo gestion_cabanas.py: contiene la función principal para levantar el sistema de gestión de cabañas. """
import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    """Levanta todo el sistema de gestión de cabañas."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_core.settings")

    try:
        django.setup()
        print("✅ Sistema de gestión de cabañas inicializado correctamente")
    except Exception as e:
        print("❌ Error al inicializar Django:", e)
        sys.exit(1)

    # Si se pasan argumentos (ej: runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
