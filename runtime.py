import os
import sys
import django
from django.core.management import execute_from_command_line

# Forzamos las rutas que Django necesita en producción
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_core.core.settings')

if __name__ == '__main__':
    django.setup()
    execute_from_command_line(sys.argv)
