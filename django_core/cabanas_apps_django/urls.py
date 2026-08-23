"""Puente de URLs para django_core"""
import importlib.util
import sys
from pathlib import Path
from django.views.generic import TemplateView
from .views import (
    AlquilerCreateView, AlquilerDeleteView, AlquilerListView, AlquilerUpdateView,
    CabanaCreateView, CabanaDeleteView, CabanaListView, CabanaUpdateView,
    ClienteCreateView, ClienteDeleteView, ClienteListView, ClienteUpdateView,
    RegistroCreateView, RegistroDeleteView, RegistroListView, RegistroUpdateView,
    ReservaCreateView, ReservaDeleteView, ReservaListView, ReservaUpdateView,
)

VIEWS_PATH = Path(__file__).resolve().parent / "cabanas_apps _django" / "views.py"
spec = importlib.util.spec_from_file_location("cabanas_apps_django_views", VIEWS_PATH)
cabanas_apps_django_views = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cabanas_apps_django_views
spec.loader.exec_module(cabanas_apps_django_views)

RENDER_PATH = Path(__file__).resolve().parent / "cabanas_apps _django" / "render.py"
render_spec = importlib.util.spec_from_file_location(
    "cabanas_apps_django_render", RENDER_PATH
)
cabanas_apps_django_render = importlib.util.module_from_spec(render_spec)
sys.modules[render_spec.name] = cabanas_apps_django_render
render_spec.loader.exec_module(cabanas_apps_django_render)

app_name = "cabanas_apps_django_urls"  # pylint: disable=invalid-name

urlpatterns = [
    path("", cabanas_apps_django_views.panel, name="panel"),
    path("render/", cabanas_apps_django_render.render_todas_las_apps, name="render_apps"),
    path(
        "todas-las-apps/",
        cabanas_apps_django_render.render_todas_las_apps,
        name="todas_las_apps",
    ),
    path("<str:app_slug>/", cabanas_apps_django_views.listar, name="listar"),
    path("<str:app_slug>/crear/", cabanas_apps_django_views.crear, name="crear"),
    path("<str:app_slug>/<int:pk>/", cabanas_apps_django_views.ver, name="ver"),
    path("<str:app_slug>/<int:pk>/editar/", cabanas_apps_django_views.editar, name="editar"),
    path("<str:app_slug>/<int:pk>/borrar/", cabanas_apps_django_views.borrar, name="borrar"),
    path("apps/", include("cabanas_apps.urls")),
    path("gestion/", include("cabanas_apps.gestion_cabanas.urls")),
    path("interfaz_gestion_cabanas/", include("django_core.cabanas_apps_django_interfaz_urls")),
    path("cabanas_app/", include("cabanas_apps.cabanas_app.urls")),



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
