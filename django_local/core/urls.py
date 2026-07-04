"""archivo de urls del proyecto django_local"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Administración Django
    path("admin/", admin.site.urls),

    # Punto de entrada de gestión
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),

    # Interfaz principal
    path("interfaz/", include("cabanas_apps.interfaz_gestion_cabanas.urls")),

    # Apps del sistema de cabañas
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("pagina_principal/", include("cabanas_apps.pagina_principal.urls")),
    path("formulario/", include("cabanas_apps.formulario.urls")),
]
