"""archivo de modelos para la aplicación de cabañas"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum



class Chatbot(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="Chatbot Cabañas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.Chatbot


class Cabana(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="cabanas")

    def __str__(self) -> str:
        return f"{self.nombre} - Capacidad: {self.capacidad} - Precio: ${self.precio_base}"


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="clientes")

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"




    def __str__(self) -> str:
        return f"Alquileres {self.id}"
    
    class Alquileres(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_clientes = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="La cantidad de clientes debe ser al menos 1."),
            MaxValueValidator(20, message="La cantidad de clientes no puede exceder 20."),
        ]
    )
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="reservas")

    def clean(self) -> None:
        super().clean()
        if self.fecha_fin <= self.fecha_inicio:
            raise ValidationError(_("La fecha de fin debe ser posterior a la fecha de inicio."))

        if self.cantidad_clientes > self.cabana.capacidad:
            raise ValidationError(_("La cantidad de clientes excede la capacidad de la cabaña."))

        reservas_solapadas = Reserva.objects.filter(
            cabana=self.cabana,
            fecha_inicio__lte=self.fecha_fin,
            fecha_fin__gte=self.fecha_inicio,
        ).exclude(id=self.id)

        if reservas_solapadas.exists():
            raise ValidationError(_("La cabaña ya está reservada para las fechas seleccionadas."))

    def __str__(self) -> str:
        return f"Reserva {self.id}"


class RegistroDiario(models.Model):
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="registros")
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="registros")

    def __str__(self) -> str:
        return f"Registro {self.id} - {self.fecha}"


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name="factura")
    fecha_emision = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagada = models.BooleanField(default=False)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="facturas")

    def __str__(self) -> str:
        return f"Factura {self.id}"


class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(
        max_length=20,
        choices=[
            ("efectivo", "Efectivo"),
            ("tarjeta", "Tarjeta"),
            ("transferencia", "Transferencia"),
        ],
    )
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="pagos")

    def __str__(self) -> str:
        return f"Pago {self.id}"

    def clean(self) -> None:
        super().clean()
        if self.monto > self.factura.monto_total:
            raise ValidationError(_("El monto del pago no puede exceder el monto total de la factura."))

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        pagos_totales = self.factura.pagos.aggregate(total=Sum("monto"))["total"] or 0
        if pagos_totales >= self.factura.monto_total:
            self.factura.pagada = True
            self.factura.save(update_fields=["pagada"])
