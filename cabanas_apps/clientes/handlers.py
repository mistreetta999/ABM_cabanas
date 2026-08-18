""" archivo handles.py: contiene las funciones que manejan las solicitudes HTTP para la aplicación de gestión de cabañas. """
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
class handles:
    """Clase handles para manejar las solicitudes HTTP."""
    def __init__(self):
        pass
# -------------------
# PÁGINA PRINCIPAL
# -------------------
def pagina_principal()->HttpResponse:
    return HttpResponse("Bienvenida al sistema de gestión de cabañas")
# cabanas
def listar_clientes()->HttpResponse:
    return HttpResponse("lista de cabanas")

# -------------------
# RESERVAS
# -------------------
def listar_reservas():
    reservas = [
        {"id": 1, "cliente": "Carolina", "Cabanas
": "Premium"},
        {"id": 2, "cliente": "Juan", "Cabanas
": "Standard"},
    ]
    # reservas is a list, so safe must be False to allow non-dict JSON responses
    return JsonResponse(reservas, safe=False)

def detalle_reserva(reserva_id):
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

def crear_reserva( cliente_id, cabana_id):
    return HttpResponse(f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_reserva( reserva_id):
    return HttpResponse(f"Reserva {reserva_id} borrada")

# -------------------
# ALQUILERES
# -------------------
def listar_alquileres():
    alquileres = [
        {"id": 1, "cliente": "Pedro", "Cabanas
": "Suite"},
        {"id": 2, "cliente": "Lucía", "Cabanas
": "Deluxe"},
    ]
    return JsonResponse(alquileres, safe=False)

def detalle_alquiler(reserva_id):
    return HttpResponse(f"Detalle del alquiler {reserva_id}")

def crear_alquiler( cliente_id, cabana_id):
    return HttpResponse(f"Alquiler creado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_alquiler( reserva_id):
    return HttpResponse(f"Alquiler {reserva_id} borrado")

# -------------------
# PAGOS
# -------------------
def listar_pagos():
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    return JsonResponse(pagos, safe=False)

def detalle_pago( reserva_id):
    return HttpResponse(f"Detalle del pago para reserva {reserva_id}")

def crear_pago( cliente_id, cabana_id):
    return HttpResponse(f"Pago registrado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_pago( reserva_id):
    return HttpResponse(f"Pago de reserva {reserva_id} borrado")
