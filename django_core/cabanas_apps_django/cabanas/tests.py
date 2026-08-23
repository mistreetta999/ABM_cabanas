from django.test import TestCase
from .models import Cabana

class CabanaModelTest(TestCase):
    def setUp(self):
        # Creamos una instancia de prueba
        self.cabana = Cabana.objects.create(
            nombre="Cabaña Test",
            capacidad=4,
            descripcion="Cabaña de prueba",
            precio_por_noche=1500.00,
            disponible=True
        )

    def test_cabana_str(self):
        # Verificamos que el método __str__ devuelva el nombre
        self.assertEqual(str(self.cabana), "Cabaña Test")

    def test_cabana_disponible(self):
        # Verificamos que la cabaña esté marcada como disponible
        self.assertTrue(self.cabana.disponible)
