"""views cabanas_api"""
from django.http import HttpResponse
APP_NAME = "cabanas_api"


def index(request):
    return HttpResponse("Bienvenidos, Django está funcionando en cabanas_api!")

def gestion(request):
    return HttpResponse("Panel de gestión activo")

def pagos(request):
    return HttpResponse("Vista de Pagos")

def clientes(request):
    return HttpResponse("Vista de Clientes")
