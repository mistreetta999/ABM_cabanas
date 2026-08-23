"""
setup.py
Script de inicialización del entorno Django para el Sistema de Gestión de Cabanas.
"""

import os
import sys
import django


def inicializar(settings_module="cabanas_project.settings"):
    """
    Configura el entorno de Django con el módulo de settings indicado.
    """
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
        django.setup()
        print(f"--- Entorno Django inicializado con {settings_module} ---")
    except ImportError:
        print("Error: Django no está instalado en el entorno actual.")
        sys.exit(1)
    except Exception as exc:
        print(f"Error al configurar Django: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    # Inicializa Django con la configuración por defecto
    inicializar()
