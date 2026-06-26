from django.shortcuts import render
from django.http import HttpResponse
from .models import Cabana

def index(request):
    return HttpResponse("Vista inicial de Cabañas")

def lista_cabanas(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})
