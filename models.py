"""archivo principal models"""
from django.db import models
from django.utils import timezone
from django.http import HttpRequest, HttpResponse


class Cabanas
(models.Model):
    """ Modelo que representa una cabaña """
    id = models.AutoField(primary_key=True)  # clave primaria automática
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
    dni = models.IntegerField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    class Meta:
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
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"
    def __str__(self) -> str:
        return str(self.nombre)

class Reserva(models.Model):
    """ Modelo que representa una reserva de cabaña """
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


class Alquileres(models.Model):
    """ Modelo que representa un alquiler de cabaña """
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

    def __str__(self) -> str:
        return f"Alquiler {self.pk}"


class Pago(models.Model):
    """ Modelo que representa un pago de un alquiler """
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    def __str__(self) -> str:
        return f"Pago {self.pk}"


class Registro(models.Model):
    """ Modelo que representa un registro de actividad en el sistema """
    fecha = models.DateTimeField(default=timezone.now)
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
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
        verbose_name = "Plantilla"
        verbose_name_plural = "Plantillas"

    def __str__(self) -> str:
        return (f"Plantilla: {self.nombre} - Asunto: {self.asunto} - Fecha de creación: {self.fecha_creacion}" )
class TempaltesModels(models.Model):
    """Modelo para representar plantillas de correo electrónico."""
    nombre = models.CharField(max_length=100, unique=True)
    asunto = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Plantilla"
        verbose_name_plural = "Plantillas"

    def __str__(self) -> str:
        return (f"Plantilla: {self.nombre} - Asunto: {self.asunto} - Fecha de creación: {self.fecha_creacion}" )
class Formulario(models.Model):
    """Modelo para representar un formulario de contacto."""
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Formulario de Contacto"
        verbose_name_plural = "Formularios de Contacto"

    def __str__(self) -> str:
        return f"Formulario de {self.nombre} - Email: {self.email} - Fecha de envío: {self.fecha_envio}"    
def index(request: HttpRequest) -> HttpResponse:
    """Vista de ejemplo para la página de pagina_principal."""
    return HttpResponse("¡Bienvenido a la aplicación de gestión de cabañas!")
