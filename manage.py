""" manage.py: Arranca el proyecto Django sin excepciones. """
import os
import sys
from django.core.management import execute_from_command_line  # Import al toplevel

def main():
    """Arranca el proyecto Django sin excepciones."""
    # Ajusta el nombre del paquete al de tu carpeta real
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabanas_principal.settings")

    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado en tu entorno virtual?"
        ) from exc

if __name__ == '__main__':
    main()
