"""
Módulo central de la app gestion_cabanas.
Se encarga de inicializar la app y conectar con la interfaz principal.
"""

from django.urls import path, include
from django.shortcuts import render

# Vista principal de gestión
def pagina_principal(request):
    """
    Página principal del sistema de gestión de cabañas.
    Desde aquí se accede a todas las demás apps.
    """
    return render(request, "gestion_cabanas/pagina_principal.html")

# Rutas de la app gestion_cabanas
urlpatterns = [
    path("", pagina_principal, name="pagina_principal"),
    path("interfaz/", include("cabanas_apps.interfaz_gestion_cabanas.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_apps.urls")),
]
