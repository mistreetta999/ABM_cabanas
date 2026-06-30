"""archivo contiene los modelos del programa."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from cabanas_apps.chatbot_app.models import ChatbotResponse
from pathlib import Path

directories = Path(".").parents


class Publisher:
    
    """ esta clase es del publisher"""
    
    def __init__(self, name):
        self.name = name
    
    def publish(self, message):
        """ este metodo es para publicar"""
        print(f"{self.name} published: {message}")

    class Meta:
        """ Metadatos del modelo Publisher """
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"


class Chatbot(models.Model):
    """ esta clase es del chatbot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = "Chatbot Cabanas"
        self.descripcion = "Este es un chatbot para la gestión de Cabanas."
        self.reponses = ChatbotResponse(chatbot=self)
            
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
    descripcion = models.TextField(blank=True, null=True)
    class Meta:
        """ Metadatos del modelo Chatbot """
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"    

    def __str__(self) -> str:
        """ Representación en cadena del modelo Chatbot """
        return str(self.nombre)

    class Meta:
        """ Metadatos del modelo Chatbot """
        verbose_name = "Chatbot"
        verbose_name_plural = "Chatbots"


class Cabanas(models.Model):
    """ esta clase es de la Cabana"""
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="cabanas")
    class Meta:

        """ Metadatos del modelo Cabanas """
        verbose_name = "Cabana"
        verbose_name_minuscula = "cabana"
        verbose_name_minuscula_plural   = "cabanas"
        verbose_name_plural = "Cabanas"

    def __str__(self) -> str:
        return f"{self.nombre} - Capacidad: {self.capacidad} - Precio: ${self.precio_base}"

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
    """ Clase que representa un alquiler de Cabana. """
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
    cabana = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="alquileres")
    cantidad_clientes = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="La cantidad de clientes debe ser al menos 1."),
            MaxValueValidator(20, message="La cantidad de clientes no puede exceder 20."),
        ]
    )
    cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))
    capacidad_cabanas = int(input("Ingrese la capacidad de la cabana:2,3,4.5 "))
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="reservas")
    Cabanas=models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="alquileres")
    estado = models.BooleanField(default=False, choices=[(True, "Aceptada"), (False, "Pendiente")])
    def acepar_reserva(self):
        """ Método para aceptar la reserva. """
        self.estado = "aceptada"
        self.save()
        if self.cantidad_clientes == self.capacidad_cabanas:
            print("La reserva ha sido aceptada.")
    
    def clean(self) -> None:
        super().clean()
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin <= self.fecha_inicio:
            raise ValidationError(_("La fecha de fin debe ser posterior a la fecha de inicio."))

        if self.cantidad_clientes > self.cabana.capacidad_cabanas:  # type: ignore
            
            raise ValidationError(_("La cantidad de clientes excede la capacidad de la cabana."))
  


        reservas_solapadas = Alquileres.objects.filter(  # type: ignore
            cabana=self.cabana,
            fecha_inicio__lte=self.fecha_fin,
            fecha_fin__gte=self.fecha_inicio,
        ).exclude(id=self.id)

        if reservas_solapadas.exists():
            raise ValidationError(_("La Cabana ya está reservada para las fechas seleccionadas."))
    class Meta:
        """ Metadatos del modelo Alquileres """
        verbose_name = "Alquiler"
        verbose_name_minuscula = "alquiler"
        verbose_name_minuscula_plural = "alquileres"
        verbose_name_plural = "Alquileres"
    def __str__(self) -> str:
        return f"Reserva {self.id}"


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="reservas")
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
            raise ValidationError(_("La cantidad de clientes excede la capacidad de la Cabana."))

        reservas_solapadas = Reserva.objects.filter(  # type: ignore
            cabana=self.cabana,
            fecha_inicio__lte=self.fecha_fin,
            fecha_fin__gte=self.fecha_inicio,
        ).exclude(id=self.id)

        if reservas_solapadas.exists():
            raise ValidationError(_("La Cabana ya está reservada para las fechas seleccionadas."))
    class Meta:
        """ Metadatos del modelo Reserva """
        verbose_name = "Reserva"
        verbose_name_minuscula = "reserva"
        verbose_name_minuscula_plural = "reservas"
        verbose_name_plural = "Reservas"
   
    def __str__(self) -> str:
        return f"Reserva {self.id}"


class RegistroDiario(models.Model):
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="registros")
    fecha = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="registros")

    class Meta:
        """ Metadatos del modelo RegistroDiario """
        verbose_name = "Registro Diario"
        verbose_name_minuscula = "registro_diario"
        verbose_name_minuscula_plural = "registros_diarios"
        verbose_name_plural = "Registros Diarios"

    def __str__(self) -> str:
        return f"Registro {self.id} - {self.fecha}"


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name="factura")
    fecha_emision = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagada = models.BooleanField(default=False)
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="facturas")

    class Meta:
        """ Metadatos del modelo Factura """
        verbose_name = "Factura"
        verbose_name_minuscula = "factura"
        verbose_name_minuscula_plural = "facturas"
        verbose_name_plural = "Facturas"

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
    class Meta:
        """ Metadatos del modelo Pago """
        verbose_name = "Pago"
        verbose_name_minuscula = "pago"
        verbose_name_minuscula_plural = "pagos"
        verbose_name_plural = "Pagos"
  

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
