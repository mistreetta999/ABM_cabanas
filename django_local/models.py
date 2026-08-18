"""archivo contiene los modelos del programa."""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from pathlib import Path
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.db import models
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
directories = Path(".").parents
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Models:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ esta clase es de los modelos"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __init__(self, *args, **kwargs):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        super().__init__(*args, **kwargs)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.nombre = "Modelos Cabanas"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        self.descripcion = "Estos son los modelos para la gestión de Cabanas."  
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Chatbot(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ esta clase es del chatbot"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
 
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    nombre = models.CharField(max_length=100, default="Chatbot Cabanas")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    descripcion = models.TextField(blank=True, null=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        """ Representación en cadena del modelo Chatbot """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return str(self.nombre)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Cabanas(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ esta clase es de la Cabanas
"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    nombre = models.CharField(max_length=100, unique=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    capacidad = models.PositiveIntegerField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    descripcion = models.TextField(blank=True, null=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    disponible = models.BooleanField(default=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="cabanas")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
   
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return f"{self.nombre} - Capacidad: {self.capacidad} - Precio: ${self.precio_base}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Cliente(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ esta clase es del cliente"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    DNI = models.CharField(max_length=100)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    nombre = models.CharField(max_length=100)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    apellido = models.CharField(max_length=100)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    email = models.EmailField(unique=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    telefono = models.CharField(max_length=20, blank=True, null=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="clientes")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return f"{self.nombre} {self.apellido}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
 
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Alquileres(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ Clase que representa un alquiler de Cabanas
. """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="alquileres")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Cabanas
 = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="alquileres")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    capacidad_cabanas = models.PositiveIntegerField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    cantidad_clientes = models.PositiveIntegerField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
   
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return f"Reserva {self.id}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Reserva(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ Clase que representa una reserva de Cabanas
. """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Cabanas
 = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="reservas")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    fecha_inicio = models.DateField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    fecha_fin = models.DateField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    capacidad_cabanas= models.PositiveIntegerField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    cantidad_clientes = models.PositiveIntegerField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            return f"Reserva {self.id}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class RegistroDiario(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ class RegistrosDiarios   """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    Cabanas
 = models.ForeignKey(Cabanas, on_delete=models.CASCADE, related_name="registros")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    fecha = models.DateField()
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    observaciones = models.TextField(blank=True, null=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    reservas = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="registros")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    alquileres = models.ForeignKey(Alquileres, on_delete=models.CASCADE, related_name="registros")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="registros")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return f"Registro {self.id} - {self.fecha}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Factura(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ class factura para emitir despues del pago """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name="factura")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    alquileres = models.OneToOneField(
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        Alquileres,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        on_delete=models.CASCADE,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        related_name="factura_alquiler",
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    )
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    fecha_emision = models.DateField(auto_now_add=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    pagada = models.BooleanField(default=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="facturas")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
  
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) -> str:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return f"Factura {self.id}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
class Pago(models.Model):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ class pagos de facturas """
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    id = models.AutoField(primary_key=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="pagos")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    fecha_pago = models.DateField(auto_now_add=True)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    metodo = models.CharField(
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        max_length=20,
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        choices=[
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            ("efectivo", "Efectivo"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            ("tarjeta", "Tarjeta"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
            ("transferencia", "Transferencia"),
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        ],
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    )
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    chatbot = models.ForeignKey(Chatbot, on_delete=models.SET_NULL, null=True, related_name="pagos")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
  
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    def __str__(self) :
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        return f"Pago {self.id}"
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
