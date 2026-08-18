from django.test import TestCase
from .models import ChatbotResponse

class ChatbotAppTests(TestCase):
    def setUp(self):
        # Crear un objeto de prueba
        ChatbotResponse.objects.create(
            pregunta="¿Cuál es tu nombre?",
            respuesta="Soy el chatbot de Cabañas."
        )

    def test_respuesta_se_guarda(self):
        # Verificar que la respuesta se guardó correctamente
        respuesta = ChatbotResponse.objects.get(pregunta="¿Cuál es tu nombre?")
        self.assertEqual(respuesta.respuesta, "Soy el chatbot de Cabañas.")

    def test_respuesta_no_vacia(self):
        # Verificar que la respuesta no esté vacía
        respuesta = ChatbotResponse.objects.first()
        self.assertTrue(len(respuesta.respuesta) > 0)
