"""archivo principal models"""
from django.db import models

from django.core.validators import RegexValidator
class Publisher(models.Model):
    """Modelo publisher."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        """ meta para reconocer los terminos"""
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"

    def __str__(self) -> str:
        return "Publishe"
    
class Cabana(models.Model):
    """ Modelo que representa una cabaña """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """  
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
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """  
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class Chatbot(models.Model):
    """"Modelo para representar un chatbot."""
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)
    class Meta:
         """ class Meta para definir el nombre del modelo en singular y plural. """
         app_label = "chatbot_app"
         verbose_name = "Chatbot"
         verbose_name_plural = "Chatbots"
    def __str__(self) -> str:
        return str(self.nombre)

class Reserva(models.Model):
    """"Modelo que representa una reserva de Cabana."""
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, default="pendiente")
    observaciones = models.TextField(blank=True)
    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self) -> str:
        return f"Reserva {self.pk}"


class Alquiler(models.Model):
    """"Modelo que representa un alquiler de Cabana."""
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="alquileres")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, default="activo")
    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """  
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self) -> str:
        return f"Alquiler {self.pk}"


class Pago(models.Model):
    """"Modelo que representa un pago de un alquiler."""
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)
    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    def __str__(self) -> str:
        return f"Pago {self.pk}"


class Registro(models.Model):
    """"Modelo que representa un registro de actividad en el sistema."""
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self) -> str:
        return f"{self.modulo}: {self.responsable}"
