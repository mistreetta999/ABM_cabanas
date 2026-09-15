from django.db import models


class ChatbotResponse(models.Model):
    """Modelo que representa una respuesta del chatbot."""

    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta {self.pk}"
