from django.db import models
from django.urls import reverse


class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    dni = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    def get_absolute_url(self):
        return reverse('cliente_list')


class Cabana(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    capacidad = models.PositiveSmallIntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('cabana_list')


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.PROTECT)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['-fecha_ingreso']

    def __str__(self):
        return f'{self.cliente} - {self.cabana}'

    def get_absolute_url(self):
        return reverse('reserva_list')


class Alquiler(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cabana = models.ForeignKey(Cabana, on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f'{self.cliente} - {self.cabana} ({self.estado})'

    def get_absolute_url(self):
        return reverse('alquiler_list')


class Pago(models.Model):
    METODOS = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('tarjeta', 'Tarjeta'),
    ]

    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODOS, default='efectivo')
    comprobante = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.alquiler} - ${self.monto}'

    def get_absolute_url(self):
        return reverse('pago_list')


class Registro(models.Model):
    MODULOS = [
        ('clientes', 'Clientes'),
        ('reservas', 'Reservas'),
        ('alquileres', 'Alquileres'),
        ('pagos', 'Pagos'),
    ]

    fecha = models.DateField(auto_now_add=True)
    modulo = models.CharField(max_length=20, choices=MODULOS)
    descripcion = models.TextField()
    responsable = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.get_modulo_display()} - {self.fecha}'

    def get_absolute_url(self):
        return reverse('registro_list')
