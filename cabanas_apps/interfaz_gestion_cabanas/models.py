"""archivo principal models"""
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator


class Cabanas(models.Model):
    """ Modelo que representa una cabaña """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """class meta"""
        db_table = "cabanas"
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"
class Cliente(models.Model):
    """ Modelo que representa un cliente """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    dni = models.CharField(
        max_length=20,
        unique=True,          # obligatorio y único, pero no clave primaria
        validators=[RegexValidator(r'^\d{1,20}$', 'El DNI debe contener solo números (máx. 20).')]
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    class Meta:
        """class meta"""
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
         """ class Meta para definir el nombre del modelo en singular y plural. """
         verbose_name = "Chatbot"
         verbose_name_plural = "Chatbots"
    def __str__(self):
        return str(self.nombre)

class Reserva(models.Model):
    """class reserva"""
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="reservas")
    Cabanas = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, default="pendiente")
    observaciones = models.TextField(blank=True)
    class Meta:
        """class meta"""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva {self.pk}"


class Alquiler(models.Model):
    """ class alquiler"""
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    Cabanas = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="alquileres")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, default="activo")
    class Meta:
        """ class meta"""
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"Alquiler {self.pk}"


class Pago(models.Model):
    """class pago"""
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)
    class Meta:
        """class meta"""
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    def __str__(self):
        return f"Pago {self.pk}"


class Registro(models.Model):
    """class registro"""
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        """class meta"""
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f"{self.modulo}: {self.responsable}"
class Usuarios (models.Model):
    """class usuario"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    class Meta:
        """class meta"""
        verbose_name = "Usuario"

    def __str__(self):
        return str(self.user)
