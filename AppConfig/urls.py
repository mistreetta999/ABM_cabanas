"""URLs de la aplicación AppConfig."""

from django.urls import path

from . import views

app_name = "appconfig"

urlpatterns = [
    path("", views.config_list, name="config_list"),
    path("nuevo/", views.config_create, name="config_create"),
    path("<int:pk>/", views.config_detail, name="config_detail"),
    path("<int:pk>/editar/", views.config_update, name="config_update"),
    path("<int:pk>/borrar/", views.config_delete, name="config_delete"),
]
