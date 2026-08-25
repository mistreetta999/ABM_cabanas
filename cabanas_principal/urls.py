

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Apps propias
    path("cabanas/", include("django_core.cabanas_apps_django.cabanas.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),
    path("registros/", include("django_core.cabanas_apps_django.registros.urls")),
    path("usuarios/", include("django_core.cabanas_apps_django.usuarios.urls")),
    path("pagos/", include("django_core.cabanas_apps_django.pagos.urls")),
    path("facturas/", include("django_core.cabanas_apps_django.facturas.urls")),
    path("gestion/", include("django_core.cabanas_apps_django.gestion_cabanas.urls")),
    path("interfaz/", include("django_core.cabanas_apps_django.interfaz_gestion_cabanas.urls")),
    path("web/", include("django_core.cabanas_apps_django.web.urls")),
    path("chatbot/", include("django_core.cabanas_apps_django.chatbot_app.urls")),
]
