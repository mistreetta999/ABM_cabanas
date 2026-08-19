"""Puente de URLs para django_core/cabanas_apps _django."""
import importlib.util
import sys
from pathlib import Path

from django.urls import include, path


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

app_name = "cabanas_apps_django_bridge"

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
]
