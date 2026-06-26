""""Views for the cabanass_api project.
"""
from django.http import HttpResponse
from django.shortcuts import render
from cabanas_apps.models import Cabanas

from pathlib import Path

directories = Path(".").parents
def index(request):
    return HttpResponse("cabanas API funcionando correctamente")

def lista_cabanass(request):
    cabanass = Cabanas.objects.all()
    return render(request, "Cabanas_api/lista.html", {"cabanass": cabanass})
