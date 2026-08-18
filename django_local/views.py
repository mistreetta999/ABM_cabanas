"""views dajango"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.shortcuts import render
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from pathlib import Path
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.http import HttpResponse,HttpResponse
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
from django.shortcuts import render
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def pagina_principal(request:Any)->HttpResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """def pagina principal"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return render(request, "pagina_principal.html")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
# Vista de prueba
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def home(_request:Any)->HttpResponse:
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """ def home"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return HttpResponse("Servidor Django Local funcionando correctamente")
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",

  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
# Ejemplo de vista para listar cabañas
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
def lista_cabanas(request):
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    """def listas"""
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    cabanas = [
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        {"nombre": "Cabaña 1", "capacidad": 2},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
        {"nombre": "Cabaña 2", "capacidad": 3},
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    ]
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})
  # Apps propias
    "cabanas_apps.cabanas_app",  
    "cabanas_apps.cabanas",
