"""
Module for shortcut functions to handle cabanas rendering and retrieval.
"""
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from cabanas_apps.reservas.models import Reserva


def home(_request):
    """View function for the home page of the cabanas API."""
    return JsonResponse({"mensaje": "API de Cabañas funcionando"})

@csrf_exempt
def crear_reserva(request):
    """View function to create a new reservation."""
    if request.method == "POST":
        data = json.loads(request.body)
        reserva = Reserva.objects.create(
            cliente=data.get("cliente"),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            cabana=data.get("cabana"),
            estado="pendiente"
        )
        return JsonResponse({"id": reserva.id, "mensaje": "Reserva creada"})
    return JsonResponse({"error": "Método no permitido"}, status=405)

# ... y lo mismo para alquiler, pago, factura, actividades
