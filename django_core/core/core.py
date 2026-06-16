import os
import sys


class Management:
    """
    Clase central para la gestión del framework Django.
    Define y encapsula la configuración del entorno y la ejecución de comandos.
    """

    def __init__(self, settings_module="cabanas_project.settings"):
        """
        Inicializa la instancia de gestión.
        :param settings_module: Ruta al archivo de configuración de Django.
        """
        self.settings_module = settings_module
        # Calculamos la raíz del proyecto (2 niveles arriba: de core/ a django/ a raíz/)
        self.project_root = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", ".."
        ))

    def setup_environment(self):
        """
        Configura el PYTHONPATH y la variable de entorno de Django.
        Esto permite que el sistema encuentre las apps en 'cabana_apps'.
        """
        # Añadir la raíz al sistema para que cabanas_project y cabana_apps sean visibles
        if self.project_root not in sys.path:
            sys.path.append(self.project_root)
        
        # Establecer el módulo de configuración (Settings)
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_module)
        
        print(f"[*] Entorno preparado en: {self.project_root}")
        print(f"[*] Usando configuraciones de: {self.settings_module}")

    

    def __str__(self):
        return f"Core Management System - Root: {self.project_root}"