"""archivo principal models"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class Cabanas
:
    """ Modelo que representa una cabaña """
    id = models.IntegerField(primary_key=True)  # clave primaria automática
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "cabanas"
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"
class Cliente(models.Model):
    """ Modelo que representa un cliente """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class Chatbot(models.Model):
    """"Modelo para representar un chatbot."""
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True)
    class Meta:
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"

    def __str__(self):
        return str(self.nombre)

class Reserva(models.Model):
    """ Modelo que representa una reserva de cabaña """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="reservas")
    Cabanas
 = models.ForeignKey(Cabanas
, on_delete=models.CASCADE, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, default="pendiente")
    observaciones = models.TextField(blank=True)
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva {self.pk}"


class Alquiler(models.Model):
    """ Modelo que representa un alquiler de cabaña """
    id = models.IntegerField(primary_key=True)  # clave primaria automática
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    Cabanas
 = models.ForeignKey(Cabanas
, on_delete=models.CASCADE, related_name="alquileres")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, default="activo")
    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"Alquiler {self.pk}"


class Pago(models.Model):
    """ Modelo que representa un pago realizado por un cliente """
    id = models.IntegerField(primary_key=True)  # clave primaria automática
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    def __str__(self):
        return f"Pago {self.pk}"


class Registro(models.Model):
    """ Modelo que representa un registro de actividad """
    id = models.IntegerField(primary_key=True)  # clave primaria automática
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f"{self.modulo}: {self.responsable}"
class Usuarios (models.Model):
    user = models.OneToOneField( on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.user.username


class UsuarioSistema(AbstractUser):
    dni = models.CharField(max_length=20, unique=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    rol = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=255, blank=True)  # opcional
    activo = models.BooleanField(default=True)  # <-- nuevo campo

    def __str__(self):
        return f"{self.username} ({self.rol})"
