 """ archivo de urls del proyecto django_local """
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import handlers

urlpatterns = [
    path("", handlers.sistema_status, name="sistema_status"),
    path("settings/", handlers.mostrar_settings, name="mostrar_settings"),
    path("settings/apps/", handlers.listar_apps, name="listar_apps"),
    path("settings/middleware/", handlers.listar_middleware, name="listar_middleware"),
    path("settings/db/", handlers.db_config, name="db_config"),
    path("settings/static/", handlers.static_config, name="static_config"),
    path("settings/media/", handlers.media_config, name="media_config"),
]


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
    path("template/", include("cabanas_apps.template_app.urls")),
    path("interfaz_gestion_cabanas/", include("cabanas_apps.interfaz_gestion_cabanas.urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("pagina_principal/", include("cabanas_apps.pagina_principal.urls")),
    path("formulario/", include("cabanas_apps.formulario.urls"))
    
]


urlpatterns = [
    # Administración Django
    path("admin/", admin.site.urls),

    # Punto de entrada de gestión
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),

    # Interfaz principal
    path("interfaz/", include("cabanas_apps.interfaz_gestion_cabanas.urls")),

 
]