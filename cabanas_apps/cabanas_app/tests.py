""" archivo tests para la app cabanas_app """
from django.test import TestCase
from .models import Cliente

class ClienteTestCase(TestCase):
    """Test case para Cliente model"""
    def test_crear_cliente(self):
        """Prueba la creación de un cliente y verifica sus atributos."""
        cliente = Cliente(
            nombre="Carolina",
            apellido="Test",
            email="carolina@test.com"
        )
        self.assertEqual(cliente.nombre, "nombre")
        self.assertEqual(cliente.apellido, "Test")
        self.assertEqual(cliente.email, "nombre@test.com")
