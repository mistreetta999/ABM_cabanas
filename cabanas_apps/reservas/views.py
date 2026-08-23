"""Este archivo contiene las vistas para la aplicación de reservas.
"""
import os 
from  pathlib import Path

from django.shortcuts import render
from .models import Reserva

def lista_reservas(request):
    """Vista para mostrar la lista de reservas."""
    reservas = Reserva.objects.all()
    return render(request, "reservas/panel.html", {"reservas": reservas})
