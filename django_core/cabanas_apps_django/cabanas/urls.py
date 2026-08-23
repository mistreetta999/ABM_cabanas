"""URLs de cabanas relacionadas con alquileres y clientes."""
from django.urls import include, path
from django.views.generic import TemplateView
from . import views

app_name = "cabanas"

urlpatterns = [
    # Listado de cabañas
    path("cabanas/", views.CabanaListView.as_view(), name="cabanas_list"),

    # Página principal con TemplateView
    path("pagina_principal/", TemplateView.as_view(template_name="pagina_principal.html"), name="pagina_principal"),

    # CRUD de cabañas
    path("crear/", views.CabanaCreateView.as_view(), name="crear_cabana"),
    path("<int:pk>/", views.CabanaDetailView.as_view(), name="detalle_cabana"),
    path("<int:pk>/editar/", views.CabanaUpdateView.as_view(), name="editar_cabana"),
    path("<int:pk>/eliminar/", views.CabanaDeleteView.as_view(), name="eliminar_cabana"),

    # Enlaces a otras apps
    path("alquileres/", include("django_core.cabanas_apps_django.alquileres.urls")),
    path("clientes/", include("django_core.cabanas_apps_django.clientes.urls")),
]
