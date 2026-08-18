""""Módulo de handles para el sistema de gestión de cabañas."""
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.urls import path
from typing import Any

apps_name = "cabanas_apps"  # pylint: disable=invalid-name


def sistema_status(request):
    """Devuelve el estado del sistema"""
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse({"status": "OK"})

def mostrar_settings(request):
    """Muestra la configuración del proyecto"""
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    settings_dict = {setting: getattr(settings, setting) for setting in dir(settings) if setting.isupper()}
    return JsonResponse(settings_dict)

def db ():
    """Muestra la configuración de la base de datos"""
    db_dict = {setting: getattr(settings, setting) for setting in dir(settings) if setting.isupper()}
    return JsonResponse(db_dict)



# -------------------
# PÁGINA PRINCIPAL
# -------------------
def pagina_principal():
    """Renderiza la página principal del sistema de gestión de cabañas."""
    return HttpResponse("Bienvenida al sistema de gestión de cabañas")

# -------------------
# RESERVAS
# -------------------
def listar_reservas():
    """Lista todas las reservas disponibles."""
    reservas = [
        {"id": 1, "cliente": "Carolina", "Cabanas
": "Premium"},
        {"id": 2, "cliente": "Juan", "Cabanas
": "Standard"},
    ]
    return JsonResponse(reservas, safe=False)

def detalle_reserva( reserva_id):
    """Muestra el detalle de una reserva específica."""
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

def crear_reserva( cliente_id, cabana_id):
    """Crea una nueva reserva para un cliente en una cabaña específica."""
    return HttpResponse(f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_reserva( reserva_id):
    """Borra una reserva específica."""
    return HttpResponse(f"Reserva {reserva_id} borrada")

# -------------------
# ALQUILERES
# -------------------
def listar_alquileres():
    """Lista todos los alquileres disponibles."""
    alquileres = [
        {"id": 1, "cliente": "Pedro", "cabaña": "Suite"},
        {"id": 2, "cliente": "Lucía", "cabaña": "Deluxe"},
    ]
    # JsonResponse requires a dict unless safe=False is set for lists
    return JsonResponse(alquileres, safe=False)

def detalle_alquiler(reserva_id):
    """Muestra el detalle de un alquiler específico."""
    return HttpResponse(f"Detalle del alquiler {reserva_id}")

def crear_alquiler(cliente_id, cabana_id):
    """Crea un nuevo alquiler para un cliente en una cabaña específica."""
    return HttpResponse(f"Alquiler creado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_alquiler( reserva_id):
    """Borra un alquiler específico."""
    return HttpResponse(f"Alquiler {reserva_id} borrado")

# -------------------
# PAGOS
# -------------------
def listar_pagos():
    """Lista todos los pagos disponibles."""
    pagos = [
        {"id": 1, "reserva": 1, "monto": 5000},
        {"id": 2, "reserva": 2, "monto": 7000},
    ]
    # Return as a dict to keep JsonResponse safe=True (lists are unsafe by default)
    return JsonResponse({"pagos": pagos}, safe=True)

def detalle_pago( reserva_id):
    """Muestra el detalle de un pago específico."""
    return HttpResponse(f"Detalle del pago para reserva {reserva_id}")

def crear_pago( cliente_id, cabana_id):
    """Crea un nuevo pago para un cliente en una cabaña específica."""
    return HttpResponse(f"Pago registrado para cliente {cliente_id} en cabaña {cabana_id}")

def borrar_pago( reserva_id):
    """Borra un pago específico."""
    return HttpResponse(f"Pago de reserva {reserva_id} borrado")

