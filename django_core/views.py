"""Este archivo contiene las vistas de la app registros."""
from django.shortcuts import render

# Vista para la página principal
def pagina_principal(request):
    """Renderiza la página principal."""
    return render(request, "pagina_principal.html")

# Vista para la sección de gestión
def gestion(request):
    """Renderiza la página de gestión."""
    return render(request, "gestion.html")
