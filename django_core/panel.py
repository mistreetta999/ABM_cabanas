""" panel admin"""
from django.shortcuts import render





def render_panel(request, template_name: str, context: dict = None):
    """
    Función genérica para renderizar paneles dentro del proyecto.
    - request: objeto HttpRequest
    - template_name: ruta del template (ej: 'cabanas/panel.html')
    - context: diccionario opcional con datos para la plantilla
    """
    if context is None:
        context = {}
    return render(request, template_name, context)


# Ejemplo de uso en una vista:
# from django_core.panel import render_panel
#
# def panel_cabanas(request):
#     return render_panel(request, "cabanas/panel.html", {"titulo": "Panel de Cabañas"})
