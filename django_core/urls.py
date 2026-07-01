""""este archivo contiene las urls de la app registros"""
from django.contrib import admin
from django.urls import include, path

from cabanas_api.views import pagina_principal

urlpatterns = [
    
    # Panel de administración
    path("admin/", admin.site.urls),

    # Home / panel principal
    path("", include("cabanas_apps.urls")),

    # Chatbot
    path("chatbot/", include("chatbot.urls")),
    #pagina principal
    path("pagina_principal/", pagina_principal, name="pagina_principal"),

    # Módulos internos
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    # App principal de Cabanas
    path("cabanas/", include("cabanas.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),

    path("admin/", admin.site.urls),
    path("", handles.pagina_principal, name="pagina_principal"),
    path("formularios/", handles.Formularios_panel_Django, name="formularios_panel"),
    path("imagenes/", handles.imagen_panel_Django, name="imagenes_panel"),
    path("cabanas/", handles.cabanas_panel_Django, name="cabanas_panel"),
    path("reservas/", handles.reservas_panel_Django, name="reservas_panel"),
    path("chatbot/", handles.chatbot_panel_Django   , name="chatbot_panel"),

]
