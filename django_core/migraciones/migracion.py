import django
import models from models
class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)