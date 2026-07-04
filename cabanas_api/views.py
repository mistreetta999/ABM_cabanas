"""views cabanas_api"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from .models import Reserva, Alquiler, Pago, Factura, ActividadCabana



# Vista de inicio simple
def home(_request):
    """Vista de inicio de la API de Cabañas."""
    return JsonResponse({"mensaje": "API de Cabañas funcionando"})


# --- RESERVAS ---
@csrf_exempt
def crear_reserva(request):
    """Crea una nueva reserva en el sistema."""
    if request.method == "POST":
        data = json.loads(request.body)
        reserva = Reserva.objects.create(
            cliente=data.get("cliente"),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin"),
            cabana=data.get("cabana"),
            estado="pendiente"
        )
        ActividadCabana.objects.create(
            tipo="Reserva",
            descripcion=f"Reserva creada para {reserva.cliente}",
            fecha=timezone.now(),
            usuario=reserva.cliente,
            referencia_id=reserva.id
        )
        return JsonResponse({"id": reserva.id, "mensaje": "Reserva creada"})
    return JsonResponse({"error": "Método no permitido"}, status=405)


# --- ALQUILERES ---
@csrf_exempt
def crear_alquiler(request):
    if request.method == "POST":
        data = json.loads(request.body)
        alquiler = Alquiler.objects.create(
            cliente=data.get("cliente"),
            cabana=data.get("cabana"),
            fecha=data.get("fecha"),
            monto=data.get("monto")
        )
        ActividadCabana.objects.create(
            tipo="Alquiler",
            descripcion=f"Alquiler registrado para {alquiler.cliente}",
            fecha=timezone.now(),
            usuario=alquiler.cliente,
            referencia_id=alquiler.id
        )
        return JsonResponse({"id": alquiler.id, "mensaje": "Alquiler registrado"})


# --- PAGOS ---
@csrf_exempt
def registrar_pago(request):
    if request.method == "POST":
        data = json.loads(request.body)
        pago = Pago.objects.create(
            cliente=data.get("cliente"),
            monto=data.get("monto"),
            metodo=data.get("metodo", "efectivo")
        )
        ActividadCabana.objects.create(
            tipo="Pago",
            descripcion=f"Pago registrado de {pago.cliente}",
            fecha=timezone.now(),
            usuario=pago.cliente,
            referencia_id=pago.id
        )
        return JsonResponse({"id": pago.id, "mensaje": "Pago registrado"})


# --- FACTURAS ---
@csrf_exempt
def generar_factura(request):
    if request.method == "POST":
        data = json.loads(request.body)
        factura = Factura.objects.create(
            numero=data.get("numero"),
            cliente=data.get("cliente"),
            monto_total=data.get("monto_total"),
            detalle=data.get("detalle", "")
        )
        ActividadCabana.objects.create(
            tipo="Factura",
            descripcion=f"Factura generada para {factura.cliente}",
            fecha=timezone.now(),
            usuario=factura.cliente,
            referencia_id=factura.id
        )
        return JsonResponse({"id": factura.id, "mensaje": "Factura generada"})
def obtener_actividades(request):
    actividades = ActividadCabana.objects.all().order_by('-fecha')
    actividades_list = [
        {
            "tipo": actividad.tipo,
            "descripcion": actividad.descripcion,
            "fecha": actividad.fecha,
            "usuario": actividad.usuario,
            "referencia_id": actividad.referencia_id
        }
        for actividad in actividades
    ]
    return JsonResponse({"actividades": actividades_list})
def pagina_principal(request):
    """Vista para la página principal."""
    return JsonResponse({"mensaje": "Bienvenido a la página principal de Cabañas"})