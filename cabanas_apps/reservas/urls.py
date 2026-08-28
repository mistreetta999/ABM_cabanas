"""
Pruebas unitarias para la aplicación Reservas.
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from clientes.models import Cliente
from cabanas.models import Cabana
from .models import Reserva
from .reservas import ReservaService


class ReservaServiceTest(TestCase):
    """Pruebas para la lógica de negocio de reservas."""

    def setUp(self):
        # Crear datos iniciales
        self.cliente = Cliente.objects.create(nombre="Carolina", apellido="Test", email="carolina@test.com")
        self.cabana = Cabana.objects.create(nombre="Cabaña Test", capacidad=4, precio_noche=1000)

    def test_crear_reserva_valida(self):
        """Debe crear una reserva válida sin solapamientos."""
        inicio = date.today()
        fin = inicio + timedelta(days=3)
        reserva = ReservaService.crear(self.cliente.id, self.cabana.id, inicio, fin, monto_total=3000)
        self.assertEqual(reserva.estado, "pendiente")
        self.assertEqual(reserva.duracion(), 3)

    def test_crear_reserva_fecha_invalida(self):
        """Debe lanzar error si la fecha fin es anterior a inicio."""
        inicio = date.today()
        fin = inicio - timedelta(days=1)
        with self.assertRaises(ValidationError):
            ReservaService.crear(self.cliente.id, self.cabana.id, inicio, fin, monto_total=1000)

    def test_crear_reserva_solapada(self):
        """Debe lanzar error si ya existe una reserva en el rango."""
        inicio = date.today()
        fin = inicio + timedelta(days=2)
        ReservaService.crear(self.cliente.id, self.cabana.id, inicio, fin, monto_total=2000)

        # Intentar crear otra reserva en el mismo rango
        with self.assertRaises(ValidationError):
            ReservaService.crear(self.cliente.id, self.cabana.id, inicio, fin, monto_total=2000)

    def test_confirmar_reserva(self):
        """Debe cambiar el estado de la reserva a confirmada."""
        inicio = date.today()
        fin = inicio + timedelta(days=2)
        reserva = ReservaService.crear(self.cliente.id, self.cabana.id, inicio, fin, monto_total=2000)
        ReservaService.confirmar(reserva.id)
        reserva.refresh_from_db()
        self.assertEqual(reserva.estado, "confirmada")

    def test_cancelar_reserva(self):
        """Debe cambiar el estado de la reserva a cancelada."""
        inicio = date.today()
        fin = inicio + timedelta(days=2)
        reserva = ReservaService.crear(self.cliente.id, self.cabana.id, inicio, fin, monto_total=2000)
        ReservaService.cancelar(reserva.id)
        reserva.refresh_from_db()
        self.assertEqual(reserva.estado, "cancelada")

    def test_finalizar_reserva(self):
        """Debe cambiar el estado de la reserva a finalizada."""
        inicio = date.today()
        fin =