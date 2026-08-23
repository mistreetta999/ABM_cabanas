import os
import sys

class Management:
    """
    Clase que define y gestiona la lógica administrativa del proyecto.
    Esta es la definición de 'management' que el sistema utilizará.
    """
    def __init__(self, settings_module="cabanas_project.settings"):
        self.settings_module = settings_module
        # Calculamos la raíz del proyecto (2 niveles arriba de este archivo)
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    def prepare_system(self):
        """Configura los paths y las variables de entorno."""
        if self.project_root not in sys.path:
            sys.path.append(self.project_root)
        
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_module)

    def execute_command(self, args):
        """
        Método que invoca la utilidad de comandos de Django
        usando la configuración definida en esta clase.
        """
        try:
            from django.core.management import execute_from_command_line
            execute_from_command_line(args)
        except ImportError as exc:
            raise ImportError(
                "Error: No se pudo encontrar Django. Revisa tu entorno virtual."
            ) from exc

    def info(self):
        return f"Management configurado para: {self.settings_module}"
