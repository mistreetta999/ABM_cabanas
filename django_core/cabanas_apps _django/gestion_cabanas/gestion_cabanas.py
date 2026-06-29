from django.db import models
from django.core.validators import RegexValidator

class Cabana(models.Model):
    """Modelo que representa una cabaña"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "cabanas"
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    """Modelo que representa un cliente"""
    dni = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(r'^\d{1,20}$', 'El DNI debe contener solo números (máx. 20).')]
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class Chatbot(models.Model):
    """Modelo para representar un chatbot"""
    nombre = models.CharField(max_length=100, default="Chatbot Cabañas")
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    ESTADOS_RESERVA = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
    ]

    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=30, choices=ESTADOS_RESERVA, default="pendiente")
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.cabana}"


class Alquiler(models.Model):
    ESTADOS_ALQUILER = [
        ("activo", "Activo"),
        ("finalizado", "Finalizado"),
        ("cancelado", "Cancelado"),
    ]

    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="alquileres")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=30, choices=ESTADOS_ALQUILER, default="activo")

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"Alquiler {self.pk} - {self.cliente}"


class Pago(models.Model):
    METODOS_PAGO = [
        ("efectivo", "Efectivo"),
        ("tarjeta", "Tarjeta"),
        ("transferencia", "Transferencia"),
    ]

    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30, choices=METODOS_PAGO)
    comprobante = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"Pago {self.pk} - {self.metodo}"


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
