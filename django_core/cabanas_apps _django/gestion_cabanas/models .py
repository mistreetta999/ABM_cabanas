"""archivo principal models"""

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

class Cabanas(models.Model):
    """Modelo que representa una cabaña."""

    id = models.AutoField(primary_key=True)  # clave primaria automática
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    """Modelo que representa un cliente."""

    id = models.AutoField(primary_key=True)  # clave primaria automática
    dni = models.CharField(
        max_length=20,
        unique=True,  # obligatorio y único, pero no clave primaria
        validators=[RegexValidator(r"^\d{1,20}$", "El DNI debe contener solo números (máx. 20).")],
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class Chatbot(models.Model):
    """Modelo para representar un chatbot."""

    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)


class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña."""

    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name="reservas")
    Cabanas = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, default="pendiente")
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.Cabanas} ({self.fecha_ingreso} - {self.fecha_salida})"


class Alquiler(models.Model):
    """Modelo que representa un alquiler de cabaña."""

    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    Cabanas= models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="alquileres")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, default="activo")

    def __str__(self):
        return f"Alquiler {self.pk}"


class Pago(models.Model):
    """Modelo que representa un pago de un alquiler."""

    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Pago {self.pk}"


class Registro(models.Model):
    """Modelo que representa un registro de actividad en el sistema."""

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.modulo}: {self.responsable}"
class Factura(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateField(default=timezone.now)
    cliente = models.ForeignKey("Clientes", on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Factura {self.numero} - Cliente: {self.cliente} - Total: ${self.monto_total}"
class usuarios (models.models):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Email: {self.email}"   
