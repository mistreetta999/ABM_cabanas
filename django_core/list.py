from django.shortcuts import render
from django_core.models import Cabanas

def cabana_list(request):
    # Consultamos todas las cabañas
    cabanas = Cabana.objects.all()
    # Renderizamos la plantilla list.html con el contexto
    return render(request, "cabanas/list.html", {"cabanas": cabanas})
