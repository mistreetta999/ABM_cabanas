from decimal import Decimal

"""archivo  models"""
from django.db import models
from django.utils import timezone


class Cabana(models.Model):
    """cabana"""

    id = models.AutoField(primary_key=True)  # clave primaria automática
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """class Meta para definir el nombre del modelo en singular y plural."""

        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"

    def __str__(self) -> str:
        """Devuelve una representación legible de la cabaña."""
        return f"{self.nombre} - Capacidad: {self.capacidad}"


class Cliente(models.Model):
    """Modelo que representa un cliente"""

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return str(self.nombre)


class Alquiler(models.Model):
    """Modelo que representa un alquiler de cabaña"""

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} - {self.fecha_inicio} a {self.fecha_fin}"


class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña"""

    cliente = models.ForeignKey(
        "Cliente", on_delete=models.CASCADE, related_name="reservas"
    )
    Cabanas = models.ForeignKey(
        Cabana, on_delete=models.CASCADE, related_name="reservas"
    )
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, default="pendiente")
    observaciones = models.TextField(blank=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        """Configuración del modelo Reserva."""

        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva {self.pk}"


class Pago(models.Model):
    """Modelo que representa un pago de un alquiler"""

    alquiler = models.ForeignKey(
        "alquileres.Alquiler",  # referencia correcta al modelo Alquiler
        on_delete=models.CASCADE,
        related_name="pagos",
    )
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)

    class Meta:
        """Metadatos del modelo Pago"""

        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-fecha"]  # ordena por fecha descendente

    def __str__(self) -> str:
        return f"Pago {self.pk} - {self.monto} ({self.metodo})"


class Registro(models.Model):
    """Modelo que representa un registro de actividad en el sistema"""

    fecha = models.DateTimeField(default=timezone.now)
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Metadatos del modelo Registro"""

        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self) -> str:
        return f"{self.modulo}: {self.responsable}"


class TemplatesModels(models.Model):
    """Modelo para representar plantillas de correo electrónico."""

    nombre = models.CharField(max_length=100, unique=True)
    asunto = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadatos del modelo TemplatesModels"""

        verbose_name = "Plantilla"
        verbose_name_plural = "Plantillas"

    def __str__(self) -> str:
        return f"Plantilla: {self.nombre} - Fecha de creación: {self.fecha_creacion}"


class TempltesModels(models.Model):
    """Modelo para representar plantillas de correo electrónico."""

    nombre = models.CharField(max_length=100, unique=True)
    asunto = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadatos del modelo TempaltesModels"""

        verbose_name = "Plantilla"
        verbose_name_plural = "Plantillas"

    def __str__(self) -> str:
        return f"Plantilla: {self.nombre} - Asunto: {self.asunto} - Fecha de creación: {self.fecha_creacion}"


class Formulario(models.Model):
    """Modelo para representar un formulario de contacto."""

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Metadatos del modelo Formulario"""

        verbose_name = "Formulario de Contacto"
        verbose_name_plural = "Formularios de Contacto"

    def __str__(self) -> str:
        return f"Formulario de {self.nombre} - Email: {self.email} - Fecha de envío: {self.fecha_envio}"


class ChatbotResponse(models.Model):
    """
    Respuestas del chatbot a los mensajes del cliente.
    """

    chatbot = models.ForeignKey(
        "Chatbot", on_delete=models.CASCADE, related_name="responses"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Metadatos del modelo ChatbotResponse"""

        verbose_name = "Chatbot Response"
        verbose_name_plural = "Chatbot Responses"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Response from {self.chatbot} at {self.created_at}"


class Message(models.Model):
    """
    Mensajes enviados por el cliente o el chatbot.
    """

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(
        max_length=50, choices=[("cliente", "Cliente"), ("chatbot", "Chatbot")]
    )

    class Meta:
        """Metadatos del modelo Message"""

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender}"


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

    chatbot = models.ForeignKey(
        Chatbot, on_delete=models.CASCADE, related_name="handles"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="handles"
    )
    cliente = models.ForeignKey(
        "Cliente",
        on_delete=models.CASCADE,
        related_name="chatbot_messages",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.chatbot} - {self.message}"


class Factura(models.Model):
    """facturas"""

    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="facturas"
    )
    cabana = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="facturas"
    )
    fecha_emision = models.DateField(auto_now_add=True)
    alquiler = models.ForeignKey(
        Alquiler, on_delete=models.CASCADE, related_name="facturas"
    )
    reserva = models.ForeignKey(
        Alquiler, on_delete=models.CASCADE, related_name="facturas"
    )
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    pagos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """nombre"""

        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"


class DetalleFactura(models.Model):
    """detalles de facturas"""

    factura = models.ForeignKey(
        Factura, on_delete=models.CASCADE, related_name="detalles"
    )
    descripcion = models.CharField(max_length=200)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total_linea = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """nombre"""

        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Factura"

    def __str__(self):
        return f"{self.descripcion} ({self.cantidad} x {self.precio_unitario})"
