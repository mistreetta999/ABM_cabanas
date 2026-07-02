# cabanas_api/handlers.py
from django.http import JsonResponse, HttpResponse

def pagina_principal(request):
    return HttpResponse("Bienvenida a la API de Cabañas")

def listar_reservas(request):
    reservas = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Cabaña 1"},
        {"id": 2, "cliente": "Juan", "cabaña": "Cabaña 2"},
    ]
    return JsonResponse(reservas, safe=False)

def detalle_reserva(request, reserva_id):
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

def crear_reserva(request, cliente_id, cabana_id):
    return HttpResponse(
        f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}"
    )

def borrar_reserva(request, reserva_id):
    return HttpResponse(f"Reserva {reserva_id} borrada")

def listar_pagos(request):
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    return JsonResponse(pagos, safe=False)
