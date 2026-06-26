""""Views for the cabanass_api project.
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenida Carolina 💙, tu app cabanas_api está funcionando.")

def clientes(request):
    return HttpResponse("Vista de Clientes")

def reservas(request):
    return HttpResponse("Vista de Reservas")

def alquileres(request):
    return HttpResponse("Vista de Alquileres")

def registros(request):
    return HttpResponse("Vista de Registros")
