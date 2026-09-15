"""
Handlers para la aplicación Chatbot (pública).
Se encargan de procesar mensajes, generar respuestas y manejar historial.
"""

from django.utils import timezone
from registros.models import Registro


class ChatbotHandler:
    """Handler principal para el chatbot público."""

    @staticmethod
    def procesar_mensaje(usuario, mensaje: str) -> dict:
        """
        Procesa un mensaje entrante del usuario y devuelve una respuesta.
        """
        respuesta = ChatbotHandler.generar_respuesta(mensaje)

        # Guardar en registros para historial
        Registro.objects.create(
            usuario=usuario,
            tipo="chatbot",
            descripcion=f"Usuario dijo: {mensaje} | Bot respondió: {respuesta}",
            fecha=timezone.now(),
        )

        return {"mensaje": mensaje, "respuesta": respuesta}

    @staticmethod
    def generar_respuesta(mensaje: str) -> str:
        """
        Genera una respuesta básica según el contenido del mensaje.
        (Aquí podrías integrar IA, reglas o APIs externas).
        """
        mensaje = mensaje.lower()

        if "hola" in mensaje:
            return "¡Hola! ¿Cómo puedo ayudarte con tu reserva de cabañas?"
        elif "disponibilidad" in mensaje:
            return "Puedes consultar disponibilidad en la sección 'Reservas' del sitio."
        elif "precio" in mensaje:
            return "Los precios dependen de la cabaña y la temporada. ¿Quieres que te muestre opciones?"
        elif "gracias" in mensaje:
            return "¡De nada! Estoy aquí para ayudarte."
        else:
            return "No entendí bien tu consulta, ¿podrías reformularla?"

    @staticmethod
    def historial(usuario) -> list:
        """
        Devuelve el historial de conversaciones del usuario.
        """
        registros = Registro.objects.filter(usuario=usuario, tipo="chatbot").order_by(
            "-fecha"
        )
        return [{"fecha": r.fecha, "descripcion": r.descripcion} for r in registros]
