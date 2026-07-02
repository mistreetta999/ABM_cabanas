# cabanas_apps/handlers.py
from django.http import HttpResponse, JsonResponse

# Página principal
def pagina_principal(request):
    return HttpResponse("Bienvenida a la gestión de cabañas")

# -------------------
# RESERVAS
# -------------------
def listar_reservas(request):
    reservas = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Cabaña 1"},
        {"id": 2, "cliente": "Juan", "cabaña": "Cabaña 2"},
    ]
    return JsonResponse(reservas, safe=False)

def detalle_reserva(request, reserva_id):
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

def crear_reserva(request, cliente_id, cabana_id):
    return HttpResponse(f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_reserva(request, reserva_id):
    return HttpResponse(f"Reserva {reserva_id} borrada")

# -------------------
# ALQUILERES
# -------------------
def listar_alquileres(request):
    alquileres = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Premium"},
        {"id": 2, "cliente": "Pedro", "cabaña": "Standard"},
    ]
    return JsonResponse(alquileres, safe=False)

def detalle_alquiler(request, reserva_id):
    return HttpResponse(f"Detalle del alquiler {reserva_id}")

def crear_alquiler(request, cliente_id, cabana_id):
    return HttpResponse(f"Alquiler creado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_alquiler(request, reserva_id):
    return HttpResponse(f"Alquiler {reserva_id} borrado")

# -------------------
# PAGOS
# -------------------
def listar_pagos(request):
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    return JsonResponse(pagos, safe=False)

def detalle_pago(request, reserva_id):
    return HttpResponse(f"Detalle del pago para reserva {reserva_id}")

def crear_pago(request, cliente_id, cabana_id):
    return HttpResponse(f"Pago registrado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_pago(request, reserva_id):
    return HttpResponse(f"Pago de reserva {reserva_id} borrado")
