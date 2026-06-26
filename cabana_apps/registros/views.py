from django.shortcuts import render
from .models import ActividadCabana

def lista_actividades(request):
    actividades = ActividadCabana.objects.all()
    return render(request, "registros/lista.html", {"actividades": actividades})
