"""Este script de Python permite ejecutar las migraciones """
import os
import django
from django.core.management import call_command

# 1. Configura el entorno de Django (reemplaza 'mi_proyecto.settings' por tu settings.py real)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

def ejecutar_migraciones():
    """Función para ejecutar las migraciones de Django."""
    try:
        print("Iniciando aplicación de migraciones...")
        
        # 2. Ejecuta python manage.py migrate
        call_command('migrate')
        
        print("¡Migraciones aplicadas con éxito!")
    except django.core.management.CommandError as e:
        print(f"Ocurrió un error al migrar: {e}")

if __name__ == '__main__':
    ejecutar_migraciones()
