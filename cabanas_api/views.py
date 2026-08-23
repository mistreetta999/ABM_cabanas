"""Vistas JSON simples para cabanas_api."""
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(_request: HttpRequest) -> JsonResponse:
    """Vista de pagina_principal de la API."""
    return JsonResponse({"mensaje": "API de Cabanas funcionando"})


def pagina_principal(_request: HttpRequest) -> JsonResponse:
    """Vista para la pagina principal de la API."""
    return JsonResponse({"mensaje": "Bienvenido a la API de Cabanas"})


@csrf_exempt
def crear_reserva(request: HttpRequest) -> JsonResponse:
    """Endpoint placeholder para crear reservas."""
    if request.method != "POST":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
    return JsonResponse({"mensaje": "Reserva recibida"})


@csrf_exempt
def crear_alquiler(request: HttpRequest) -> JsonResponse:
    """Endpoint placeholder para crear alquileres."""
    if request.method != "POST":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
    return JsonResponse({"mensaje": "Alquiler recibido"})


@csrf_exempt
def registrar_pago(request: HttpRequest) -> JsonResponse:
    """Endpoint placeholder para registrar pagos."""
    if request.method != "POST":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
    return JsonResponse({"mensaje": "Pago recibido"})


@csrf_exempt
def generar_factura(request: HttpRequest) -> JsonResponse:
    """Endpoint placeholder para generar facturas."""
    if request.method != "POST":
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
    return JsonResponse({"mensaje": "Factura recibida"})


def obtener_actividades(_request: HttpRequest) -> JsonResponse:
    """Devuelve una lista vacia de actividades."""
    return JsonResponse({"actividades": []})
