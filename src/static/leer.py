"""
Script para cargar datos de prueba en el sistema de cabañas.
"""

import os
import django

# Configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cabana_proyect.settings")
django.setup()

from django_local.models import Cliente, Cabana, Reserva
from datetime import date

def run():
    # Crear clientes de prueba
    cliente1 = Cliente.objects.create(nombre="Ana", apellido="Pérez", email="ana@example.com")
    cliente2 = Cliente.objects.create(nombre="Luis", apellido="Gómez", email="luis@example.com")

    # Crear cabañas de prueba
    cabana1 = Cabana.objects.create(nombre="Cabaña Río", capacidad=4, precio_noche=15000)
    cabana2 = Cabana.objects.create(nombre="Cabaña Montaña", capacidad=6, precio_noche=20000)

    # Crear reservas de prueba
    Reserva.objects.create(
        cliente=cliente1,
        cabana=cabana1,
        fecha_inicio=date(2026, 9, 1),
        fecha_fin=date(2026, 9, 5),
        monto_total=60000,
        estado="confirmada"
    )

    Reserva.objects.create(
        cliente=cliente2,
        cabana=cabana2,
        fecha_inicio=date(2026, 9, 10),
        fecha_fin=date(2026, 9, 15),
        monto_total=100000,
        estado="pendiente"
    )

    print("✅ Datos de prueba cargados correctamente.")


if __name__ == "__main__":
    run()
