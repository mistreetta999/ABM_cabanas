from django.urls import path
from .views import (
    FacturaListView,
    FacturaDetailView,
    FacturaCreateView,
    FacturaUpdateView,
    FacturaDeleteView,
)

app_name = "facturas"

urlpatterns = [
    path("", FacturaListView.as_view(), name="factura_list"),
    path("<int:pk>/", FacturaDetailView.as_view(), name="factura_detail"),
    path("crear/", FacturaCreateView.as_view(), name="factura_create"),
    path("<int:pk>/editar/", FacturaUpdateView.as_view(), name="factura_update"),
    path("<int:pk>/eliminar/", FacturaDeleteView.as_view(), name="factura_delete"),
]
