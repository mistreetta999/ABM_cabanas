from cabanas_apps.models import Alquiler, Reserva
from django.http import HttpRecuest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from .models import ChatbotResponse


@require_POST
def crear_reserva(request, cliente_id, cabana_id):
    reserva = Reserva.objects.create(cliente_id=cliente_id, cabana_id=cabana_id)
    return JsonResponse({"mensaje": "Reserva creada", "id": reserva.id})


def listar_reservas(request):
    reservas = list(Reserva.objects.values("id", "cliente__nombre", "cabana__nombre"))
    return JsonResponse(reservas, safe=False)


def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return JsonResponse(
        {
            "id": reserva.id,
            "cliente": reserva.cliente.nombre,
            "cabana": reserva.cabana.nombre,
            "fecha_ingreso": reserva.fecha_ingreso,
            "fecha_salida": reserva.fecha_salida,
        }
    )


@require_POST
def borrar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.delete()
    return JsonResponse({"mensaje": f"Reserva {reserva_id} borrada"})
