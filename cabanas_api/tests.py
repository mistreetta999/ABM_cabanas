""" archivo tests """

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Reserva, Alquiler, Pago, Factura, Registros, ActividadCabana


class ReservaTests(TestCase):
    """ Clase de prueba para el modelo Reserva """

    def test_crear_reserva(self):
        """ Prueba crear una reserva """
        reserva = Reserva.objects.create(
            cliente="Juan Pérez",
            fecha_inicio="2026-07-01",
            fecha_fin="2026-07-05",
            Cabanas
="Cabanas
 1"
        )
        self.assertEqual(reserva.cliente, "Juan Pérez")
        self.assertEqual(reserva.estado, "pendiente")


class AlquilerTests(TestCase):
    """" Clase de prueba para el modelo Alquiler """

    def test_crear_alquiler(self):
        """ Prueba crear un alquiler """
        alquiler = Alquiler.objects.create(
            cliente="Ana Gómez",
            Cabanas
="Cabanas
 2",
            fecha=timezone.now().date(),
            monto=1500.00
        )
        self.assertEqual(alquiler.Cabanas
, "Cabanas
 2")
        self.assertEqual(float(alquiler.monto), 1500.00)


class PagoTests(TestCase):
    """" Clase de prueba para el modelo Pago """

    def test_registrar_pago(self):
        """ Prueba registrar un pago """
        pago = Pago.objects.create(
            cliente="Carlos López",
            monto=2000.00,
            metodo="tarjeta"
        )
        self.assertEqual(pago.metodo, "tarjeta")
        self.assertEqual(float(pago.monto), 2000.00)


class FacturaTests(TestCase):
    """" Clase de prueba para el modelo Factura """

    def test_generar_factura(self):
        """ Prueba generar una factura """
        factura = Factura.objects.create(
            numero="F001",
            cliente="María Díaz",
            monto_total=3500.00,
            detalle="Factura de prueba"
        )
        self.assertEqual(factura.numero, "F001")
        self.assertEqual(float(factura.monto_total), 3500.00)


class ActividadTests(TestCase):
    """" Clase de prueba para el modelo ActividadCabana """

    def test_registrar_actividad(self):
        """ Prueba registrar una actividad """
        actividad = ActividadCabana.objects.create(
            tipo="Reserva",
            descripcion="Reserva de prueba",
            usuario="Tester",
            referencia_id=1,
            origen="sqlite"
        )
        self.assertEqual(actividad.tipo, "Reserva")
        self.assertIn("Reserva", str(actividad))
