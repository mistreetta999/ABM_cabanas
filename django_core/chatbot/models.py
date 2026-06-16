from django.db import models


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message: {self.content[:80]}"


class Chatbot(models.Model):
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class ChatbotHandler(models.Model):
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name="handlers")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="handlers")

    def __str__(self):
        return f"{self.chatbot} - {self.message}"
