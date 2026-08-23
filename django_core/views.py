from django.http import HttpResponse
from django.shortcuts import render

# Vista principal
def index(request):
    return HttpResponse("Bienvenida a la gestión de cabañas")

# Vistas de cabañas
def lista_cabanas(request):
    return HttpResponse("Listado de cabañas")

def detalle_cabana(request, cabana_id):
    return HttpResponse(f"Detalle de la cabaña {cabana_id}")

# Vistas de reservas
def lista_reservas(request):
    return HttpResponse("Listado de reservas")

def detalle_reserva(request, reserva_id):
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

# Vistas de clientes
def lista_clientes(request):
    return HttpResponse("Listado de clientes")

def detalle_cliente(request, cliente_id):
    return HttpResponse(f"Detalle del cliente {cliente_id}")

# Vistas de pagos
def lista_pagos(request):
    return HttpResponse("Listado de pagos")

def detalle_pago(request, pago_id):
    return HttpResponse(f"Detalle del pago {pago_id}")

# Vistas de alquileres
def lista_alquileres(request):
    return HttpResponse("Listado de alquileres")

def detalle_alquiler(request, alquiler_id):
    return HttpResponse(f"Detalle del alquiler {alquiler_id}")
