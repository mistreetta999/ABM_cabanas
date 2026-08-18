from django.test import TestCase
from .models import Cabanas


class CabanaTestCase(TestCase):
    def test_crear_cabana(self):
        Cabanas
 = Cabanas
.objects.create(
            nombre="Cabanas
 Test",
            capacidad=4,
            precio_por_noche=1000.00,
            disponible=True
        )
        self.assertEqual(Cabanas
.nombre, "Cabanas
 Test")
