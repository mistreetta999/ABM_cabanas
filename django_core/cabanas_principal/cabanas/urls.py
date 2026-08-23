""""URL configuration for the cabanas app."""
from django.urls import path
from .views import views
app_name = "cabanas"  # pylint: disable=invalid-name
urlpatterns = [
    # Listado de cabañas
    path('cabanas/', views.CabanaListView.as_view(), name='cabanas_list'),
    path('', views.CabanaListView.as_view(), name='cabanas_list'),

    # Detalle de una cabaña
    path('<int:pk>/', views.CabanaDetailView.as_view(), name='cabanas_detail'),

    # Crear nueva cabaña
    path('nueva/', views.CabanaCreateView.as_view(), name='cabanas_create'),

    # Editar cabaña existente
    path(
        '<int:pk>/editar/',
        views.CabanaUpdateView.as_view(),
        name='cabanas_update'
    ),

    # Eliminar cabaña
    path(
        '<int:pk>/eliminar/',
        views.CabanaDeleteView.as_view(),
        name='cabanas_delete'
    ),
]
