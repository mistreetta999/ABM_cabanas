from django.shortcuts import render
from django.http import JsonResponse
from cabanas_apps.cabanas.models import Cabana

def panel_gestion(request):
    return render(request, "cabanas/panel.html")

def lista_cabanas(request):
    cabanas = Cabana.objects.all().values("id", "nombre", "ubicacion", "capacidad", "precio_por_noche")
    return JsonResponse(list(cabanas), safe=False)
