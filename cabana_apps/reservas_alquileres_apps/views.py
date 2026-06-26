"""Views for the reservas_alquileres_apps application.
"""
from django.shortcuts import render
from .models import Reserva, Alquiler

def reservas_list(request):
    reservas = Reserva.objects.all()
    return render(request, "reservas_alquileres/reservas_list.html", {"reservas": reservas})

def alquileres_list(request):
    alquileres = Alquiler.objects.all()
    return render(request, "reservas_alquileres/alquileres_list.html", {"alquileres": alquileres})
