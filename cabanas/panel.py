# cabanas/panel.py

from django.shortcuts import render

def pagina_principal(request):
    """
    Renderiza la página principal del sistema de gestión de cabañas.
    """
    return render(request, "pagina_principal.html")


def panel_app(request, template_name: str, context: dict = None):
    """
    Función genérica para renderizar paneles de las distintas apps.
    Ejemplo: cabanas/panel.html, reservas/panel.html, clientes/panel.html
    """
    if context is None:
        context = {}
    return render(request, template_name, context)
