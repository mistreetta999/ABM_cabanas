from decimal import Decimal
""" models django"""
from django.db import models

class Cabana(models.Model):
    """ class cabana"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField(default=1)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(f"{self.nombre} (Capacidad: {self.capacidad})")


class Cliente(models.Model):
    """ class cliente"""
    nombre_apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return str(self.nombre_apellido)


class Reserva(models.Model):
    """Reserva de una cabaña realizada por un cliente."""
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Reserva {self.pk} - {getattr(self.cliente, 'nombre_apellido', '')}"


class Alquilres(models.Model):
    """ class alquileres"""
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Reserva {self.pk} - {getattr(self.cliente, 'nombre_apellido', '')}"

class Registros(models.Model):
    """"class registros"""
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        cliente_nombre = getattr(self.cliente, 'nombre_apellido', '')
        return str(f"Reserva {self.pk} - {cliente_nombre}")


class ChatbotResponse(models.Model):
    """
    Respuestas del chatbot a los mensajes del cliente.
    """
    chatbot = models.ForeignKey("Chatbot", on_delete=models.CASCADE, related_name="responses")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Metadatos del modelo ChatbotResponse """
        verbose_name = "Chatbot Response"
        verbose_name_plural = "Chatbot Responses"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(f"Response from {self.chatbot} at {self.created_at}")

class Message(models.Model):
    """
    Mensajes enviados por el cliente o el chatbot.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=50, choices=[("cliente", "Cliente"), ("chatbot", "Chatbot")])

    class Meta:
        """ class meta"""
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.sender)


class Chatbot(models.Model):
    """
    Representa el chatbot dentro de la aplicación.
    """
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.nombre)


class ChatbotHandler(models.Model):
    """
    Relación entre el chatbot y los mensajes.
    """
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE, related_name="handles")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="handles")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="chatbot_messages", null=True, blank=True)

    def __str__(self) -> str:
        return str(f"{self.chatbot} - {self.message}")

