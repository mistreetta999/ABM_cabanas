"""archivo contiene los modelos del programa."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from pathlib import Path

from chatbot.models import ChatbotResponse

directories = Path(".").parents

class Chatbot(models.Model):
    """ esta clase es del chatbot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = "Chatbot Cabañas"
        self.descripcion = "Este es un chatbot para la gestión de cabañas."
        self.reponses = ChatbotResponse(chatbot=self)
            
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="Chatbot Cabañas")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        """ Representación en cadena del modelo Chatbot """
        return str(self.nombre)

    class Meta:
        """ Metadatos del modelo Chatbot """
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"


class Cabanas(models.Model):
    """ esta clase es de la cabaña"""
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="cabanas")

    def __str__(self) -> str:
        return f"{self.nombre} - Capacidad: {self.capacidad} - Precio: ${self.precio_base}"
    class Meta:
        """ Metadatos del modelo Cabanas """
        verbose_name = "Cabana"
        verbose_name_minuscula = "cabana"
        verbose_name_minuscula_plural   = "cabanas"
        verbose_name_plural = "Cabanas"


class Cliente(models.Model):
    """ esta clase es del cliente"""
    id = models.AutoField(primary_key=True)
    DNI = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="clientes")

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    class Meta:
        """ Metadatos del modelo Cliente """
        verbose_name = "Cliente"
        verbose_name_minuscula = "cliente"
        verbose_name_minuscula_plural = "clientes"
        verbose_name_plural = "Clientes"


class Alquileres(models.Model):
    """ Clase que representa un alquiler de cabaña. """
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    cabana = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="alquileres")
    cantidad_clientes = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="La cantidad de clientes debe ser al menos 1."),
            MaxValueValidator(20, message="La cantidad de clientes no puede exceder 20."),
        ]
    )
    capacidad_cabanas = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="reservas")

    def clean(self) -> None:
        super().clean()
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin <= self.fecha_inicio:
            raise ValidationError(_("La fecha de fin debe ser posterior a la fecha de inicio."))

        if self.cantidad_clientes > self.cabana.capacidad:  # type: ignore
            raise ValidationError(_("La cantidad de clientes excede la capacidad de la cabana."))
  


        reservas_solapadas = Alquileres.objects.filter(  # type: ignore
            cabana=self.cabana,
            fecha_inicio__lte=self.fecha_fin,
            fecha_fin__gte=self.fecha_inicio,
        ).exclude(id=self.id)

        if reservas_solapadas.exists():
            raise ValidationError(_("La cabaña ya está reservada para las fechas seleccionadas."))

    def __str__(self) -> str:
        return f"Reserva {self.id}"


class Reserva(models.Model):
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

        if self.cantidad_clientes > self.cabana.capacidad:  # type: ignore
            raise ValidationError(_("La cantidad de clientes excede la capacidad de la cabaña."))

        reservas_solapadas = Reserva.objects.filter(  # type: ignore
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
        if self.monto > self.factura.monto_total:  # type: ignore
            raise ValidationError(_("El monto del pago no puede exceder el monto total de la factura."))

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        pagos_totales = self.factura.pagos.aggregate(total=Sum("monto"))["total"] or 0  # type: ignore
        if pagos_totales >= self.factura.monto_total:  # type: ignore
            self.factura.pagada = True  # type: ignore
            self.factura.save(update_fields=["pagada"])  # type: ignore
