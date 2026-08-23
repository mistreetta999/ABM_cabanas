# cabanas_api/handles.py
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import TemplateView
from .models import Reserva, Pago, Cabanas
, Alquiler, Factura, Registros, ActividadCabana    
def pagina_principal():
    return HttpResponse("Bienvenida a la API de Cabañas")

def listar_reservas():
    reservas = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Cabaña 1"},
        {"id": 2, "cliente": "Juan", "cabaña": "Cabaña 2"},
    ]
    return JsonResponse(reservas, safe=False)

def detalle_reserva(reserva_id):
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

def crear_reserva(cliente_id, cabana_id):
    return HttpResponse(
        f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}"
    )

def borrar_reserva(reserva_id):
    return HttpResponse(f"Reserva {reserva_id} borrada")

def listar_pagos():
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    return JsonResponse(pagos, safe=False)

def listar_cabanas(cabana_id):
    return HttpResponse(f"Detalle de la cabaña {cabana_id}")

def listar_alquileres(listar_alquileres_id):
    return HttpResponse(f"Detalle del alquiler {listar_alquileres_id}")
