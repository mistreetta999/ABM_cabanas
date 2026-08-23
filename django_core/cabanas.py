from django .contrib import interfaz_gestion_cabanas
from django.urls import path,include


urlpatterns = [
    
    path ('interfaz_gestion_cabanas/', interfaz_gestion_cabanas.site.urls),
    path ('',views.index,name='index'),
]
urlpatterns = [
    
    path ('interfaz_gestion_cabanas/', interfaz_gestion_cabanas.site.urls),
    path ('',views.view_cabanas,name='cabanas'),

]
urlpatterns = [
    
    path ('interfaz_gestion_cabanas/', interfaz_gestion_cabanas.site.urls),
    path ('',views.confirma_borrar,name='confirma_borrar'),
]
urlpatterns = [
    
    path ('interfaz_gestion_cabanas/', interfaz_gestion_cabanas.site.urls),
    path ('',views.formulario,name='formulario'),
]
urlpatterns = [
    
    path ('interfaz_gestion_cabanas/', interfaz_gestion_cabanas.site.urls),
    path ('',views.lista,name='lista'),
]
