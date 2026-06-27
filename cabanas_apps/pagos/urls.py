""" archivo de urls de la app pagos
"""
from django.urls import path
from .views import PagoListView

APP_NAME = "pagos"

urlpatterns = [
    path("list/", PagoListView.as_view(), name="pago_list"),
]
