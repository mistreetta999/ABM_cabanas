"""Este archivo contiene las urls de la app cabanas."""
from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    AlquilerCreateView, AlquilerDeleteView, AlquilerListView, AlquilerUpdateView,
    CabanaCreateView, CabanaDeleteView, CabanaListView, CabanaUpdateView,
    ClienteCreateView, ClienteDeleteView, ClienteListView, ClienteUpdateView,
    RegistroCreateView, RegistroDeleteView, RegistroListView, RegistroUpdateView,
    ReservaCreateView, ReservaDeleteView, ReservaListView, ReservaUpdateView,
)

app_name = "cabanas_apps_django"

urlpatterns = [
    # Página principal
    path("pagina_principal.html/", TemplateView.as_view(template_name="pagina_principal.html"), name="pagina_principal_html"),
    path("pagina_principal.html", TemplateView.as_view(template_name="pagina_principal.html"), name="pagina_principal_html_sin_barra"),

    # Facturas
    path("facturas/", include("facturas.urls")),

    # Apps y API
    path("apps/", include("cabanas_apps.urls")),
    path("api/", include("cabanas_api.urls")),

    # Clientes
    path("cabanas_api/clientes/", ClienteListView.as_view(), name="cliente_list"),
    path("cabanas_api/clientes/nuevo/", ClienteCreateView.as_view(), name="cliente_create"),
    path("cabanas_api/clientes/<int:pk>/editar/", ClienteUpdateView.as_view(), name="cliente_update"),
    path("cabanas_api/clientes/<int:pk>/borrar/", ClienteDeleteView.as_view(), name="cliente_delete"),

    # Cabañas
    path("cabanas_api/cabanas/", CabanaListView.as_view(), name="cabana_list"),
    path("cabanas_api/cabanas/nueva/", CabanaCreateView.as_view(), name="cabana_create"),
    path("cabanas_api/cabanas/<int:pk>/editar/", CabanaUpdateView.as_view(), name="cabana_update"),
    path("cabanas_api/cabanas/<int:pk>/borrar/", CabanaDeleteView.as_view(), name="cabana_delete"),

    # Reservas
    path("cabanas_api/reservas/", ReservaListView.as_view(), name="reserva_list"),
    path("cabanas_api/reservas/nueva/", ReservaCreateView.as_view(), name="reserva_create"),
    path("cabanas_api/reservas/<int:pk>/editar/", ReservaUpdateView.as_view(), name="reserva_update"),
    path("cabanas_api/reservas/<int:pk>/borrar/", ReservaDeleteView.as_view(), name="reserva_delete"),

    # Alquileres
    path("cabanas_api/alquileres/", AlquilerListView.as_view(), name="alquiler_list"),
    path("cabanas_api/alquileres/nuevo/", AlquilerCreateView.as_view(), name="alquiler_create"),
    path("cabanas_api/alquileres/<int:pk>/editar/", AlquilerUpdateView.as_view(), name="alquiler_update"),
    path("cabanas_api/alquileres/<int:pk>/borrar/", AlquilerDeleteView.as_view(), name="alquiler_delete"),

    # Registros
    path("cabanas_api/registros/", RegistroListView.as_view(), name="registro_list"),
    path("cabanas_api/registros/nuevo/", RegistroCreateView.as_view(), name="registro_create"),
    path("cabanas_api/registros/<int:pk>/editar/", RegistroUpdateView.as_view(), name="registro_update"),
    path("cabanas_api/registros/<int:pk>/borrar/", RegistroDeleteView.as_view(), name="registro_delete"),

    # Interfaces de gestión (corrigiendo includes)
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_.interfaz_gestion_cabanas.urls")),
    path("gestion_cabanas/", include("django_core.cabanas_apps_.gestion_cabanas.urls")),
]
