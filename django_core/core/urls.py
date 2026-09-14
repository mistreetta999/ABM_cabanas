""" urls"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django_core.cabanas_apps_django.reservas.views import ReservaViewSet

router = DefaultRouter()
router.register(r"reservas", ReservaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("reservas/", include("django_core.cabanas_apps_django.reservas.urls")),
]
