"""Atajos para vistas de gestión de cabañas."""
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cabana, Cliente, Reserva

def obtener_cabana_o_404(cabana_id):
    """Atajo para obtener una cabaña o lanzar 404."""
    return get_object_or_404(Cabana, pk=cabana_id)

def crear_reserva(cliente, cabana, fecha_ingreso, fecha_salida, observaciones=""):
    """Atajo para crear una reserva rápidamente."""
    reserva = Reserva.objects.create(
        cliente=cliente,
        cabana=cabana,
        fecha_ingreso=fecha_ingreso,
        fecha_salida=fecha_salida,
        observaciones=observaciones,
        estado="pendiente"
    )
    return reserva

def redirigir_inicio():
    """Atajo para redirigir al home."""
    return redirect("home")
