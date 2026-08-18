import os
import sys
import subprocess
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class CabanasApp:
    """Clase principal para inicializar y ejecutar comandos Django."""

    def __init__(self, settings_module="cabanas_project.settings"):
        self.settings_module = settings_module
        self.project_name = "Sistema de Gestión de Cabanas"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", self.settings_module)

    def ejecutar(self):
        """Ejecuta comandos de Django usando django-interfaz_gestion_cabanas."""
        try:
            comando = ["django-interfaz_gestion_cabanas"] + sys.argv[1:] + [f"--settings={self.settings_module}"]
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
interfaz_gestion_cabanas.site.register(Publisher)
interfaz_gestion_cabanas.site.register(Contributor)
interfaz_gestion_cabanas.site.register(Book)
interfaz_gestion_cabanas.site.register(BookContributor)
interfaz_gestion_cabanas.site.register(Review)
