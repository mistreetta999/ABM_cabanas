"""URL configuration for cabana_proyect project."""
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView

app_name = "src"

# Reused template name
PAGE_TEMPLATE = "pagina_principal.html"

urlpatterns = [
    path("pagina_principal.html/", TemplateView.as_view(template_name=PAGE_TEMPLATE), name="pagina_principal_html"),
    path("pagina_principal.html", TemplateView.as_view(template_name=PAGE_TEMPLATE), name="pagina_principal_html_sin_barra"),
    path("", include("cabanas_principal.urls")),
    path("reservas/", include("cabanas_apps.reservas.urls")),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
    path("registros/", include("cabanas_apps.registros.urls")),
    path("cabanas/", include("cabanas_apps.cabanas.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz/", include("django_core.cabanas_apps_django.interfaz_gestion_cabanas.urls")),
    path("pagos/", include("cabanas_apps.pagos.urls")),
    path("chatbot/", include("cabanas_apps.chatbot_app.urls")),
    path("django_core/", include("django_core.urls")),
]
