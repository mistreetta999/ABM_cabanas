from django.test import TestCase
from .models import Cabana

class CabanaModelTest(TestCase):
    def setUp(self):
        self.cabana = Cabana.objects.create(
            nombre="Cabaña Test",
            capacidad=4,
            descripcion="Cabaña de prueba",
            precio_base=1000.00,
            disponible=True
        )

    def test_cabana_str(self):
        self.assertEqual(str(self.cabana), "Cabaña Test")

    def test_cabana_disponible(self):
        self.assertTrue(self.cabana.disponible)
