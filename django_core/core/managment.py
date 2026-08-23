import os
import sys
from typing import Any,Self
from django.core.management.base import BaseCommand
from pytz import NonExistentTimeError

class Management:
    """
    Clase de definición pura. 
    No contiene lógica de auto-ejecución para evitar recursividad.
    """
    def __init__(self, settings_name="cabanas_project.settings"):
        self.base_dir = self.execute_from_command_line
        self.settings_name = settings_name
        # Calculamos la ruta raíz subiendo dos niveles desde este archivo
        # (core/ -> django/ -> raiz)
        self.base_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", ".."
        ))

    def setup_project_paths(self):
        """Configura el entorno ."""
        if self.base_dir not in sys.path:
            sys.path.append(self.base_dir)
        
        # Seteamos la variable de entorno de Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_name)
  
    def execute_from_command_line(self) -> Any:

        """_summary_
        """    
        if self.base_dir not in sys.path:
            sys.path.append(self.base_dir)
        
        # Seteamos la variable de entorno de Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_name)
class Command(BaseCommand):
    help = "Comando de ejemplo para verificar la configuración de Django"

    def __init__(self ):
        super().__init__()
        self.management = Management()
        self.management.setup_project_paths()
    def handle(self, *args, **options)->Any:
        self.stdown.write(self.style.succsess ('Comando ejecutado '))
             
        return super().handle(*args, **options)
