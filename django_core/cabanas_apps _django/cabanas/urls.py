"""URLs legacy de cabanas relacionadas con alquileres y clientes."""
from django.urls import include, path

from cabanas_apps.cabanas import views

app_name = "cabanas"

urlpatterns = [
    path("", views.lista_cabanas, name="lista_cabanas"),
    path("pagina_principal/", views.index, name="index"),
    path("pagina-principal/", views.pagina_principal, name="pagina_principal"),
    path("crear/", views.CabanaCreateView.as_view(), name="crear_cabana"),
    path("<int:pk>/", views.CabanaDetailView.as_view(), name="detalle_cabana"),
    path("<int:pk>/editar/", views.CabanaUpdateView.as_view(), name="editar_cabana"),
    path("<int:pk>/eliminar/", views.CabanaDeleteView.as_view(), name="eliminar_cabana"),
    path("alquileres/", include("cabanas_apps.alquileres.urls")),
    path("clientes/", include("cabanas_apps.clientes.urls")),
]
