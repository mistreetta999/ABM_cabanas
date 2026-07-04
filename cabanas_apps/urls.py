from django.urls import path
from .views import (
    CabanaListView, CabanaCreateView, CabanaUpdateView, CabanaDeleteView
)

urlpatterns = [
    path("", CabanaListView.as_view(), name="cabana_list"),
    path("nueva/", CabanaCreateView.as_view(), name="cabana_create"),
    path("<int:pk>/editar/", CabanaUpdateView.as_view(), name="cabana_update"),
    path("<int:pk>/borrar/", CabanaDeleteView.as_view(), name="cabana_delete"),
]
