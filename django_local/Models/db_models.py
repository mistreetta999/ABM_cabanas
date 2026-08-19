from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} (Capacidad: {self.capacidad})"


class Cliente(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre_apellido"]

    def __str__(self):
        return self.nombre_apellido


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_personas = models.PositiveIntegerField(default=1)
    pagada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["fecha_inicio"]

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.cabana}"


class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="pagos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["fecha_pago"]

    def __str__(self):
        return f"Pago {self.id} - {self.monto} ARS"


class Factura(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="facturas")
