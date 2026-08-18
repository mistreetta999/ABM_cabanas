from django.test import TestCase
from .models import Usuario

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(username="carolina", email="carolina@example.com")

    def test_usuario_creado(self):
        usuario = Usuario.objects.get(username="carolina")
        self.assertEqual(usuario.email, "carolina@example.com")
