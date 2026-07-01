
""""handles Módulo que contiene las funciones de manejo de vistas para la interfaz de gestión de cabañas.   """
from django.shortcuts import render

def pagina_principal_html(request):
    """Renderiza la página principal"""
    return render(request, "pagina_principal.html")
def Formularios_panel_Django(request):
    """Renderiza el panel de formularios"""
    return render(request, "formularios/panel.html")

def  imagen_panel_Django(request):
    """Renderiza el panel de imágenes"""
    return render(request, "imagenes/panel.html")

def cabanas_panel_Django(request):
    """Renderiza el panel de cabañas"""
    return render(request, "cabanas/panel.html")

def reservas_panel_Django(request):
    """Renderiza el panel de reservas"""
    return render(request, "reservas/panel.html")

def alquileres_panel_Django(request):
    """Renderiza el panel de alquileres"""
    return render(request, "alquileres/panel.html")

def chatbot_panel_Django(request):
    """Renderiza el panel del chatbot"""
    return render(request, "chatbot/panel.html")
def registros_panel_Django(request):
    """Renderiza el panel de registros"""
    return render(request, "registros/panel.html")
def clientes_panel_Django(request):
    """Renderiza el panel de clientes"""
    return render(request, "clientes/panel.html")
def pagos_panel_Django(request):
    """Renderiza el panel de pagos"""
    return render(request, "pagos/panel.html")
# django_core/gestion_dango/handles.py

def pagina_principal(request):
    """Renderiza la página principal"""
    return render(request, "pagina_principal.html")

def cabanas_panel(request):
    """Renderiza el panel de cabañas"""
    return render(request, "cabanas/panel.html")

def reservas_panel(request):
    """Renderiza el panel de reservas"""
    return render(request, "reservas/panel.html")

def chatbot_panel(request):
    """Renderiza el panel del chatbot"""
    return render(request, "chatbot/panel.html")
