from django.test import TestCase
from .models import Cliente

class ClienteTestCase(TestCase):
    def test_crear_cliente(self):
        cliente = Cliente.objects.create(
            nombre="Carolina",
            apellido="Test",
            email="carolina@test.com"
        )
        self.assertEqual(cliente.nombre, "Carolina")
