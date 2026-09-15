"""test cabanas"""

# pylint: disable=E1101
from django.test import TestCase

from .models import Cabana


class CabanaModelTest(TestCase):
    """class cabanas test"""

    def setUp(self):
        self.cabana = Cabana.objects.create(
            nombre="Cabana Test",
            capacidad=4,
            descripcion="cabana 1",
            precio_por_noche=1500.00,
            disponible=True,
        )

    def test_cabana_str(self):
        """test cabanas"""
        self.assertEqual(str(self.cabana), "Cabana Test")

    def test_cabana_disponible(self):
        """test disponibilidad"""
        self.assertTrue(self.cabana.disponible)
