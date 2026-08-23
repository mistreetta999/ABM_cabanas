"""archivo principal models"""
from django.db import models
from django.core.validators import RegexValidator

class Cabana(models.Model):
    """class cabana  models"""
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    class Meta :
        """class meta para nombres"""
        vervose_name="Cabana"

    def __str__(self)->str:
        return str(self.nombre)


class Cliente(models.Model):
    """ Modelo que representa un cliente """
    dni = models.CharField(
        max_length=20,
        unique=True,          # obligatorio y único, pero no clave primaria
        validators=[RegexValidator(r'^\d{1,20}$', 'El DNI debe contener solo números (máx. 20).')]
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    class Meta:
        """"class meta para los nombre"""
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class Chatbot(models.Model):
    """"Modelo para representar un chatbot."""
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)
    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"
    def __str__(self):
        return str(self.nombre)

class Reserva(models.Model):
    """"class reservas"""
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, default="pendiente")
    observaciones = models.TextField(blank=True)
    class Meta:
        """"class meta"""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva {self.pk}"


class Alquiler(models.Model):
    """"class alquileres"""
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    cabana= models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, default="activo")
    class Meta:
        """class meta para los neombre"""
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"Alquiler {self.pk}"
class Factura(models.Model):
    """class factura"""
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """class meta"""
        verbose_name = "Factura"

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"

class Pago(models.Model):
    """"class pagos """
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    factura= models.CharField(max_length=200, blank=True)
    class Meta:
        """class meta para nombre"""
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    def __str__(self):
        return f"Pago {self.pk}"


class Registro(models.Model):
    """"class registros"""
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        """class meta para los nombres"""
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f"{self.modulo}"
