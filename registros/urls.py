from django.urls import path

from cabanas_apps.registros import views

app_name = "registros"

urlpatterns = [
    path("", views.index, name="index"),
]
