"""Vistas principales del proyecto alquileres_cabanas"""
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Vista de inicio simple"""
    return HttpResponse("Bienvenido a la gestión de cabañas")

def dashboard(request):
    """Vista que renderiza un template"""
    return render(request, "dashboard.html")
