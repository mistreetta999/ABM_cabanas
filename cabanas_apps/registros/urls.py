"""URL configuration for cabanas_apps.registros app."""
from django.urls import path

import django_core
from . import views


app_name = "registros"  # pylint: disable=invalid-name

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("actividades/", views.ActividadCabanasListView.as_view(), name="lista_actividades"),
]
