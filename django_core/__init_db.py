from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Inicializa la base de datos con migraciones."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Aplicando migraciones..."))
        call_command("migrate")
        self.stdout.write(self.style.SUCCESS("Base de datos lista."))