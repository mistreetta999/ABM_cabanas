"""URLs de la aplicación DATABASE."""

from django.urls import path
from . import views

app_name = "database"

urlpatterns = [
    path("", views.DatabaseDashboardView.as_view(), name="dashboard"),
    path("backup/", views.DatabaseBackupView.as_view(), name="backup"),
    path("restore/", views.DatabaseRestoreView.as_view(), name="restore"),
    path("status/", views.DatabaseStatusView.as_view(), name="status"),
    path("query/", views.execute_query, name="query"),
]
