from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cabanas, name='lista_cabanas'),
    path('<int:cabana_id>/', views.detalle_cabana, name='detalle_cabana'),
    path('crear/', views.crear_cabana, name='crear_cabana'),
    path('editar/<int:cabana_id>/', views.editar_cabana, name='editar_cabana'),
    path('eliminar/<int:cabana_id>/', views.eliminar_cabana, name='eliminar_cabana'),
]
