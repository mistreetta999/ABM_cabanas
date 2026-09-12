"""Vistas principales del proyecto de gestión de cabañas."""

from django.http import HttpResponse
from django.shortcuts import render

# Vista principal
def index(request):
    """
    Vista principal que muestra un mensaje de bienvenida.
    """
    return HttpResponse("Bienvenida a la gestión de cabañas")   
