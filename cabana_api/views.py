from django.http import HttpResponse
from django.shortcuts import render
from .models import Cabana

def index(request):
    return HttpResponse("Cabana API funcionando correctamente")

def lista_cabanas(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabana_api/lista.html", {"cabanas": cabanas})
