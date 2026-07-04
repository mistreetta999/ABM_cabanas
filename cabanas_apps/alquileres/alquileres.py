"""archivo de urls para la app alquileres"""
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from pathlib import Path
from logging import getLogger

LOGGER = getLogger(__name__)
from cabanas_apps.cabanas.models import Cabana
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.reservas.models import Reserva

directories = Path(".").parents

class Alquiler(models.Model):
    """class Alquiler models"""
    id = models.AutoField(primary_key=True)
    objects = models.Manager()
    cabanas = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Alquiler {self.id} - {self.reserva}"


def listar_alquileres(request):
    """Muestra todos los alquileres."""
    alquileres = Alquiler.objects.all()
    return render(request, "django", {"alquileres": alquileres})

def detalle_alquiler(request, alquiler_id):
    """Muestra el detalle de un alquiler específico."""
    alquiler = get_object_or_404(Alquiler, pk=alquiler_id)
    return render(request, "pagina_principal/detalle.html", {"alquiler": alquiler})

def crear_alquiler(request, reserva_id):
    """Crea un nuevo alquiler a partir de una reserva."""
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    cliente = reserva.cliente
    cabana = reserva.cabana

    if request.method == "POST":
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        monto_total = request.POST.get("monto_total", 0)

        alquiler = Alquiler.objects.create(
            reserva=reserva,
            cliente=cliente,
            cabana=cabana,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            monto_total=monto_total,
            estado="activo"
        )
        return redirect("detalle_alquiler", alquiler_id=alquiler.id)

    return render(request, "pagina_principal/formulario.html", {"reserva": reserva})

def borrar_alquiler(request, alquiler_id):
    """Elimina un alquiler existente."""
    alquiler = get_object_or_404(Alquiler, pk=alquiler_id)

    if request.method == "POST":
        alquiler.delete()
        return redirect("listar_alquileres")

    return render(request, "pagina_principal/confirma_borrar.html", {"alquiler": alquiler})
