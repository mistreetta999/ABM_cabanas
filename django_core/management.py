
from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = "Comando de prueba para levantar el servidor o ejecutar tareas personalizadas"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(
            f"Servidor iniciado correctamente a las {timezone.now()}"
        ))
