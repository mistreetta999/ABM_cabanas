"""Atajos para vistas de gestión de cabañas."""
from django.http import HttpResponse, JsonResponse,HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt 
from .views import Cabanas
,Clientes,Alquileres,Reservas
from .models import Cabanas
, Cliente,Reserva,Alquileres
# Vista inicial
def index(request: HttpRequest) -> HttpResponse:
    """Vista inicial de la aplicación de gestión de cabañas."""
    return HttpResponse("Vista inicial de Cabañas")

def pagina_principal(request: HttpRequest) -> HttpResponse:
    """Vista de la página principal de la aplicación."""
    return render(request, "pagina_principal.html")

# Listar cabañas
def lista_cabanas(request: HttpRequest) -> JsonResponse:
    """Vista para listar todas las cabañas disponibles."""
    cabanas = Cabanas
.objects.all()
    data = [{"id": c.id, "nombre": c.nombre, "precio": c.precio_por_noche} for c in cabanas]
    return JsonResponse({"cabanas": data})

# Detalle de cabaña
def detalle_cabana(request: HttpRequest, cabana_id: int) -> JsonResponse:
    """Vista para obtener los detalles de una cabaña específica."""
    Cabanas
 = get_object_or_404(Cabanas
, pk=cabana_id)
    return JsonResponse({
        "id": Cabanas
.id,
        "nombre": Cabanas
.nombre,
        "descripcion": Cabanas
.descripcion,
        "precio_por_noche": Cabanas
.precio_por_noche,
        "capacidad": Cabanas
.capacidad,
    })

# Crear reserva (POST)
@csrf_exempt
def reservar_cabana(request: HttpRequest, cabana_id: int, cliente_id: int) -> JsonResponse:
    """Vista para crear una reserva de cabaña."""
    if request.method == "POST":
        Cabanas
 = get_object_or_404(Cabanas
, pk=cabana_id)
        cliente = get_object_or_404(Cliente, pk=cliente_id)

        fecha_ingreso = request.POST.get("fecha_ingreso")
        fecha_salida = request.POST.get("fecha_salida")
        observaciones = request.POST.get("observaciones", "")

        reserva = crear_reserva(cliente, Cabanas
, fecha_ingreso, fecha_salida, observaciones)
        return JsonResponse({"id": reserva.id, "estado": reserva.estado})

    return HttpResponse("Usa POST para crear una reserva")
def crear_reserva(models: Cliente, Cabanas
, fecha_ingreso, fecha_salida, observaciones=""):
    """Crea una reserva usando el modelo Reserva si existe."""
    ReservaModel = getattr(models, "Reserva", None)
    if ReservaModel is None:
        raise AttributeError("El modelo Reserva no está definido en models.py")

    return ReservaModel.objects.create(
        cliente=models,
        Cabanas
=Cabanas
,
        fecha_ingreso=fecha_ingreso,
        fecha_salida=fecha_salida,
        observaciones=observaciones,
    )
# Redirigir al pagina_principal
def volver_inicio(request):
    """Vista para redirigir al pagina_principal de la aplicación."""
    return redirect("/")
@csrf_exempt
def alquileres_cabana(request, cabana_id, cliente_id):
    """Vista para crear una reserva de cabaña."""
    if request.method == "POST":
        Cabanas
 = get_object_or_404(Cabanas
, pk=cabana_id)
        cliente = get_object_or_404(Cliente, pk=cliente_id)

        fecha_ingreso = request.POST.get("fecha_ingreso")
        fecha_salida = request.POST.get("fecha_salida")
        observaciones = request.POST.get("observaciones", "")

        reserva = crear_reserva(cliente, Cabanas
, fecha_ingreso, fecha_salida, observaciones)
        return JsonResponse({"id": reserva.id, "estado": reserva.estado})
    return HttpResponse("Usa POST para crear una reserva")

def crear_alquileres(models: Cliente, Cabanas
, fecha_ingreso, fecha_salida, observaciones=""):
    """Crea un alquiler usando el modelo Alquileres si existe."""
    Alquileres = getattr(models, "Alquileres", None)
    if Alquileres is None:
        raise AttributeError("El modelo Alquileres no está definido en models.py")

    return Alquileres.objects.create(
        cliente=models,
        Cabanas
=Cabanas
,
        fecha_ingreso=fecha_ingreso,
        fecha_salida=fecha_salida,
        observaciones=observaciones,
    )
# Redirigir al pagina_principal
def volver_inicio(request):
    """Vista para redirigir al pagina_principal de la aplicación."""
    return redirect("/")
