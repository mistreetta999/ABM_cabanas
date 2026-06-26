from django.test import TestCase
from .models import Cabana

class CabanaTestCase(TestCase):
    def test_crear_cabana(self):
        cabana = Cabana.objects.create(
            nombre="Cabana Test",
            capacidad=4,
            precio_por_noche=1000.00,
            disponible=True
        )
        self.assertEqual(cabana.nombre, "Cabana Test")
