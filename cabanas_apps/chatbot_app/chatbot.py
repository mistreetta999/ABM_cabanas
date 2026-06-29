"""" archivo chatbot para respuestas"""

class ChatBot:
    """ clase para la informacion al cliente."""
    
    def __init__(self):
        """ Inicializa el chatbot con un mensaje de bienvenida."""
        self.welcome_message = (
            "💠 Bienvenidos a nuestras cabañas con piscina en el centro de Mina Clavero\n\n"
            "💝 Estamos emocionados de ofrecerte un hogar lejos de casa en el corazón de Mina Clavero. "
            "Nuestras cabañas son ideales para familias, parejas y amigos que buscan una estadía relajante y divertida.\n"
        )

    def get_info(self):
        """
        Devuelve la información principal de las cabañas.
        """
        return {
            "ubicacion": "🌎 A 200 mts de Av San Martín, Dirección de turismo, comisaría y YPF. "
                         "A 500 mts del balneario, playas centrales, Casino y paseo de artesanos.",
            "caracteristicas": [
                "Cabañas para 2 a 5 huéspedes",
                "Cocina equipada, aire acondicionado, WiFi gratuito",
                "Cochera cubierta y galería individual",
                "Piscina compartida de 9x4 metros",
                "Solárium con reposeras cómodas"
            ],
            "servicios": [
                "Asistencia turística",
                "Quincho y asadores portátiles",
                "TV smart, microondas, heladera con freezer",
                "Vajilla completa, pava eléctrica",
                "Secador de pelo y plancha bajo pedido",
                "Lavarropas compartido",
                "Parque cerrado y seguro"
            ],
            "reservas": "🟣 Reservas mediante seña únicamente",
            "restricciones": "❌ No se reciben mascotas. 👨‍👩‍👦 Niños cuentan como huéspedes",
            "contacto": "✅ WhatsApp 3544562397"
        }

    def respond(self, user_message: str) -> str:
        """
        Responde de forma básica según el mensaje del usuario.
        """
        msg = user_message.lower()
        if "precio" in msg or "tarifa" in msg:
            return "💲 Las tarifas dependen de la temporada y cantidad de huéspedes. Consultanos por WhatsApp."
        elif "ubicacion" in msg:
            return self.get_info()["ubicacion"]
        elif "servicios" in msg:
            return "\n".join(self.get_info()["servicios"])
        elif "cabañas" in msg or "caracteristicas" in msg:
            return "\n".join(self.get_info()["caracteristicas"])
        elif "reserva" in msg:
            return self.get_info()["reservas"]
        elif "contacto" in msg or "whatsapp" in msg:
            return self.get_info()["contacto"]
        else:
            return "🤖 Hola, soy el asistente de las cabañas. Preguntame por ubicación, servicios, características, reservas o contacto."
class Message :
    """ clase para los mensajes del chatbot """
    def __init__(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content
