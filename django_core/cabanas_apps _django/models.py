""""models  archivo principal"""
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        app_label = "clientes" 

    def __str__(self):
        return f"{self.nombre} {self.apellido}".strip()



class Chatbot(models.Model):
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)

    class Meta:

        verbose_name = "Chatbot"


    def __str__(self):
        return str(self.nombre)



class Cabanas
(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField(default=1)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    disponible = models.BooleanField(default=True)
    class Meta:
        app_label = "cabana_app"

    def __str__(self):
        return str(self.nombre)


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
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
    modulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f"{self.modulo}: {self.responsable}"
