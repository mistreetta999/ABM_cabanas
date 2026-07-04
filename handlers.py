# django_core/handlers.py
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.urls import path
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from . import handlers




urlpatterns = [
    path("", handlers.sistema_status, name="sistema_status"),
    path("settings/", handlers.mostrar_settings, name="mostrar_settings"),
    path("settings/apps/", handlers.listar_apps, name="listar_apps"),
    path("settings/middleware/", handlers.listar_middleware, name="listar_middleware"),
    path("settings/db/", handlers.db_config, name="db_config"),
    path("settings/static/", handlers.static_config, name="static_config"),
    path("settings/media/", handlers.media_config, name="media_config"),
]
def sistema_status(request):
    return JsonResponse({"status": "OK"})   
def handler (request,connections()):
    return handler({"status": "OK"})

def mostrar_settings(request):
    from django.conf import settings
    settings_dict = {setting: getattr(settings, setting) for setting in dir(settings) if setting.isupper()}
    return JsonResponse(settings_dict)
def db (request):
    from django.conf import settings
    db_dict = {setting: getattr(settings, setting) for setting in dir(settings) if setting.isupper()}
    return JsonResponse(db_dict)



# -------------------
# PÁGINA PRINCIPAL
# -------------------
def pagina_principal(request):
    return HttpResponse("Bienvenida al sistema de gestión de cabañas")

# -------------------
# RESERVAS
# -------------------
def listar_reservas(request):
    reservas = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Premium"},
        {"id": 2, "cliente": "Juan", "cabaña": "Standard"},
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
        {"id": 1, "cliente": "Pedro", "cabaña": "Suite"},
        {"id": 2, "cliente": "Lucía", "cabaña": "Deluxe"},
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

