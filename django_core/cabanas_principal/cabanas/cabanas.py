from django.apps import AppConfig

class CabanasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cabanas_apps.cabanas"
    verbose_name = "Gestión de Cabañas"

    def ready(self):
        """
        Método que se ejecuta cuando la app está lista.
        Aquí puedes importar señales o inicializar lógica específica.
        """
        try:
            import cabanas_apps.cabanas.signals  # ejemplo: conectar señales
        except ImportError:
            pass
