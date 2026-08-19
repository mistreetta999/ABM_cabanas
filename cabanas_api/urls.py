"""URLs de cabanas_api."""
from django.urls import include, path

from . import views

app_name = ["cabanas_api"]

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home_alias"),
    path("pagina-principal/", views.pagina_principal, name="pagina_principal.html"),
    path("reservas", views.crear_reserva, name="crear_reserva"),
    path("alquileres", views.crear_alquiler, name="crear_alquiler"),
    path("pagos", views.registrar_pago, name="registrar_pago"),
    path("facturas", views.generar_factura, name="generar_factura"),
    path("registros", views.home, name="generar_registro"),
    path("actividades/", views.obtener_actividades, name="obtener_actividades"),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("gestion_cabanas/", include("cabanas_apps.gestion_cabanas.urls")),
]
