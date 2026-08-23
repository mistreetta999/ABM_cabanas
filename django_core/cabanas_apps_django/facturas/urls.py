from django.urls import path
from facturas.views import (
    FacturaListView,
    FacturaDetailView,
    FacturaCreateView,
    FacturaUpdateView,
    FacturaDeleteView,
)

app_name = "facturas"

urlpatterns = [
    path("", FacturaListView.as_view(), name="factura_list"),
    path("crear/", FacturaCreateView.as_view(), name="factura_create"),
    path("<int:pk>/", FacturaDetailView.as_view(), name="factura_detail"),
    path("<int:pk>/editar/", FacturaUpdateView.as_view(), name="factura_update"),
    path("<int:pk>/eliminar/", FacturaDeleteView.as_view(), name="factura_delete"),
]
