"""Script de prueba para leer reservas y mostrarlas en consola."""

import os

import django

# Configuración del entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_core.config.settings")
django.setup()

from django_core.cabanas_apps_django.reservas.models import (
    Reserva,
)  # pylint: disable=wrong-import-position


def mostrar_reservas():
    """Imprime todas las reservas registradas en la base de datos."""
    for reserva in Reserva.objects.all():  # pylint: disable=no-member
        print(
            f"Reserva #{reserva.pk} - Cliente: {reserva.cliente} "
            f"Cabaña: {reserva.cabana} "
            f"Desde: {reserva.fecha_inicio} Hasta: {reserva.fecha_fin} "
            f"Estado: {reserva.estado}"
        )


if __name__ == "__main__":
    mostrar_reservas()
