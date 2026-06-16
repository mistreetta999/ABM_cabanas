"""estos son los modelos para los admin no se pueden borrar"""
from django.db import models
from typing import Any,list
from django.db_models import BaseManager
# Definición del modelo de datos
class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='cabanas/', null=True, blank=True)

   
    class Meta:
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"
        ordering = ["fecha_inicio"]


        def obtener_todas_las_cabanas() -> BaseManager[Cabana]:
            return Cabana.objects.all()

class Cliente(models.Model):
    """
    Modelo oficial de Django para la gestión de Clientes.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True, verbose_name="DNI")
    direccion = models.TextField(blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def get_full_name(self):
        """Devuelve el nombre completo del cliente.
        """
        return f"{self.nombre} {self.apellido}"

    def get_short_name(self):
        """Devuelve el nombre corto del cliente (solo el nombre)."""
        return self.nombre
    def get_contact_info(self):
        """Devuelve la información de contacto del cliente."""
        return f"Teléfono: {self.telefono}, Dirección: {self.direccion}"


class Reserva(models.Model):
    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE, related_name="reservas")
    cabana = models.ForeignKey("cabanas.Cabana", on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["fecha_inicio"]

    def __str__(self):
        return f"Reserva de {self.cliente} para {self.cabana} del {self.fecha_inicio} al {self.fecha_fin}"




class Alquileres(models.Model):
    """
     Alquileres de un cliente en una cabaña.
    """
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cliente que realiza la reserva."
    )
    cabana = models.ForeignKey(
        Cabana,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cabaña reservada."
    )
    fecha_inicio = models.DateField(
        help_text="Fecha de inicio de la reserva."
    )
    fecha_fin = models.DateField(
        help_text="Fecha de fin de la reserva."
    )
    cantidad_clientes = models.PositiveIntegerField(
        help_text="Número de clientes incluidas en la reserva."
    )
    estado = models.CharField(
        max_length=20,
        choices=[
            ("pendiente", "Pendiente"),
            ("confirmada", "Confirmada"),
            ("cancelada", "Cancelada"),
            ("finalizada", "Finalizada"),
        ],
        default="pendiente",
        help_text="Estado actual de la reserva."
    )
    creada_en = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación de la reserva."
    )
    actualizada_en = models.DateTimeField(
        auto_now=True,
        help_text="Última fecha de actualización de la reserva."
    )

    
    def Meta(self) ->list[str]:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_inicio"]
    def __str__(self):
        return (
            f"Reserva de {self.cliente} en {self.cabana} "
            f"del {self.fecha_inicio} al {self.fecha_fin} "
            f"({self.estado})"
        )
class Registros :
    def __init__(self)->Any:
        self.registros.reservas() 
        self.registros.alquileres()
        self.chatbot.consultas()
        self.registros.clientes()
        self.registros.cabanas()
        
        
class CLASSNAMEViewSet(viewsets.ModelViewSet):
            queryset = CLASSNAME.objects.all()
            serializer_class = CLASSNAMESerializer
            permission_classes = []
        
        
        
    