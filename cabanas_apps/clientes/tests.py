"""Archivo de tests para la app clientes"""
import os
from django.test import TestCase
from django.utils import timezone
from .models import Cliente, Pago, Factura
from django.contrib.auth.models import AbstractUser
class ClienteModelTest(TestCase):
    """ class cliente """
    def setUp(self):
        self.cliente = Cliente.objects.create(
            dni=12345678,
            nombre="Juan",
            apellido="Pérez",
            direccion="Calle Falsa 123",
            telefono="3512345678"
        )

    def test_cliente_str(self):
        """El método __str__ devuelve nombre, apellido y DNI"""
        self.assertEqual(str(self.cliente), "Juan Pérez - DNI: 12345678")

class PagoModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            dni=87654321,
            nombre="Ana",
            apellido="Gómez"
        )
        self.pago = Pago.objects.create(
            cliente=self.cliente,
            monto=1000.50,
            fecha=timezone.now().date()
        )

    def test_pago_relacion_cliente(self):
        """El pago está asociado al cliente correcto"""
        self.assertEqual(self.pago.cliente, self.cliente)

class FacturaModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            dni=11223344,
            nombre="Carlos",
            apellido="López"
        )
        self.factura = Factura.objects.create(
            cliente=self.cliente,
            numero="FAC-001",
            fecha=timezone.now().date(),
            total=2500.00
        )

    def test_factura_total(self):
        """La factura guarda el total correctamente"""
        self.assertEqual(self.factura.total, 2500.00)
