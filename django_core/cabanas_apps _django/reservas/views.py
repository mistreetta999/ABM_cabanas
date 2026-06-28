"""Este archivo contiene las vistas para la aplicación de reservas.
"""
from django.shortcuts import render
from .models import Reserva

def lista_reservas(request):
    """Vista para mostrar la lista de reservas."""
    reservas = Reserva
    return render(request, "reservas/lista.html", {"reservas": reservas})
