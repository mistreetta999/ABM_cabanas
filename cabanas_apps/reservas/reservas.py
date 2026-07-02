"""Este archivo contiene las vistas para la aplicación de reservas.
"""
from django.shortcuts import get_object_or_404, render, redirect
from .models import Reserva, Cliente, Cabana,Alquileres, Pago
from .models import  Cabana,Alquileres, Pago
from django.http import HttpResponse


class reservas:
    def __init__(self, cliente, cabana, fecha_ingreso, fecha_salida, observaciones):    
        self.cliente = cliente
        self.cabana = cabana
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.observaciones = observaciones
def listar_reservas(request):
    """Muestra todas las reservas."""
    reservas = Reserva.objects.all()
    return render(request, "pagina_principal/lista.html", {"reservas": reservas})

def detalle_reserva(request, reserva_id):
    """Muestra el detalle de una reserva específica."""
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, "pagina_principal/detalle.html", {"reserva": reserva})

def crear_reserva(request, cliente_id, cabana_id):
    """Crea una nueva reserva."""
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cabana = get_object_or_404(Cabana, pk=cabana_id)

    if request.method == "POST":
        fecha_ingreso = request.POST.get("fecha_ingreso")
        fecha_salida = request.POST.get("fecha_salida")
        observaciones = request.POST.get("observaciones", "")

        reserva = Reserva.objects.create(
            cliente=cliente,
            cabana=cabana,
            fecha_ingreso=fecha_ingreso,
            fecha_salida=fecha_salida,
            observaciones=observaciones,
            estado="pendiente"
        )
        return redirect("detalle_reserva", reserva_id=reserva.id)

    return render(request, "pagina_principal/formulario.html", {"cliente": cliente, "cabana": cabana})

def borrar_reserva(request,HttpRequest, reserva_id):
    """Borra una reserva específica."""
    return HttpResponse(f"Borrar reserva {reserva_id}")