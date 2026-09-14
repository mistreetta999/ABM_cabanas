""" archivo para levantar el sistema de gestión de cabañas. """
import os
import sys
import django
from django.core.management import execute_from_command_line
from django.core.exceptions import ImproperlyConfigured

def main():
    """Levanta todo el sistema de gestión de cabañas."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_core.settings")

    try:
        django.setup()
        print("✅ Sistema de gestión de cabañas  correctamente")
    except (ImproperlyConfigured, ImportError, RuntimeError) as e:
        print("❌ Error al inicializar Django:", e)
        sys.exit(1)

    # Si se pasan argumentos (ej: runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
