import os
import sys
import subprocess
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class CabanasApp:
    """Clase principal para inicializar y ejecutar comandos Django."""

    def __init__(self, settings_module="cabanas_project.settings"):
        self.settings_module = settings_module
        self.project_name = "Sistema de Gestión de Cabañas"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", self.settings_module)

    def ejecutar(self):
        """Ejecuta comandos de Django usando django-admin."""
        try:
            comando = ["django-admin"] + sys.argv[1:] + [f"--settings={self.settings_module}"]
            subprocess.run(comando)
        except Exception as exc:
            print(f"Error al ejecutar comando: {exc}")
            sys.exit(1)


def main():
    app = CabanasApp()
    app.ejecutar()


if __name__ == "__main__":
    main()

# Registrar los modelos
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
