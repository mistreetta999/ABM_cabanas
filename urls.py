"""Rutas raiz del proyecto."""
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("pagina_principal.html", TemplateView.as_view(template_name="pagina_principal.html"), name="pagina_principal_html_sin_barra"),
    path("", include("cabanas_principal.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("facturas/", include("cabanas_apps.facturas.urls")),
]
