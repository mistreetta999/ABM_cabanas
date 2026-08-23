""" Este archivo contiene los tests de la app clientes."""
from django.test import TestCase
from django.urls import reverse
from .models import Cliente
from cabanas_apps.clientes.models import Cliente
from pathlib import Path

directories = Path(".").parents
class ClienteModelTest(TestCase):
    """ Test para el modelo Cliente """
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Juan",
            apellido="Pérez",
            dni="12345678",
            email="juan@example.com",
            telefono="3511234567"
        )

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), "Juan Pérez - DNI: 12345678")

    def test_cliente_email_unico(self):
        with self.assertRaises(Exception):
            Cliente.objects.create(
                nombre="Otro",
                apellido="Cliente",
                dni="87654321",
                email="juan@example.com",  # mismo email → debe fallar
                telefono="3517654321"
            )

class ClienteViewsTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Ana",
            apellido="García",
            dni="23456789",
            email="ana@example.com",
            telefono="3519876543"
        )

    def test_cliente_list_view(self):
        url = reverse("cliente_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ana")

    def test_cliente_create_view(self):
        url = reverse("cliente_create")
        response = self.client.post(url, {
            "nombre": "Luis",
            "apellido": "Martínez",
            "dni": "34567890",
            "email": "luis@example.com",
            "telefono": "3511112222"
        })
        self.assertEqual(response.status_code, 302)  # redirección tras crear
        self.assertTrue(Cliente.objects.filter(email="luis@example.com").exists())
