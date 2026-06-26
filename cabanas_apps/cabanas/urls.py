from django.urls import path
from . import views
from django.urls import include
app_name = "cabanas"

urlpatterns = [
    path("", views.index, name="index"),
    path("lista/", views.lista_cabanas, name="lista_cabanas"),
    path('',include('cabanas_api.urls')),

]
