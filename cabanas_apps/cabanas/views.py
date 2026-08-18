from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cabanas

import json
def cabanas ()
# Listar todas las cabañas en JSON
def lista_cabanas(request:Any):
    
    cabanas = list(Cabanas
.objects.values())
    return JsonResponse({"cabanas": cabanas})

# Ver detalle de una cabaña
def detalle_cabana(request, cabana_id):
    try:
        Cabanas
 = Cabanas
.objects.get(id=cabana_id)
        return JsonResponse({
            "id": Cabanas
.id,
            "nombre": Cabanas
.nombre,
            "capacidad": Cabanas
.capacidad,
            "precio": Cabanas
.precio,
        })
    except Cabanas
.DoesNotExist:
        return JsonResponse({"error": "Cabaña no encontrada"}, status=404)

# Crear nueva cabaña (POST con JSON)
@csrf_exempt
def crear_cabana(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Cabanas
 = Cabanas
.objects.create(
            nombre=data.get("nombre"),
            capacidad=data.get("capacidad"),
            precio=data.get("precio"),
        )
        return JsonResponse({"id": Cabanas
.id, "mensaje": "Cabaña creada"})
    return HttpResponse("Método no permitido", status=405)

# Editar cabaña existente (PUT con JSON)
@csrf_exempt
def editar_cabana(request, cabana_id):
    if request.method == "PUT":
        try:
            Cabanas
 = Cabanas
.objects.get(id=cabana_id)
            data = json.loads(request.body)
            Cabanas
.nombre = data.get("nombre", Cabanas
.nombre)
            Cabanas
.capacidad = data.get("capacidad", Cabanas
.capacidad)
            Cabanas
.precio = data.get("precio", Cabanas
.precio)
            Cabanas
.save()
            return JsonResponse({"mensaje": "Cabaña actualizada"})
        except Cabanas
.DoesNotExist:
            return JsonResponse({"error": "Cabaña no encontrada"}, status=404)
    return HttpResponse("Método no permitido", status=405)

# Eliminar cabaña (DELETE)
@csrf_exempt
def eliminar_cabana(request, cabana_id):
    if request.method == "DELETE":
        try:
            Cabanas
 = Cabanas
.objects.get(id=cabana_id)
            Cabanas
.delete()
            return JsonResponse({"mensaje": "Cabaña eliminada"})
        except Cabanas
.DoesNotExist:
            return JsonResponse({"error": "Cabaña no encontrada"}, status=404)
    return HttpResponse("Método no permitido", status=405)
