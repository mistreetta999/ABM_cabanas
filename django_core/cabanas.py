from django .contrib import admin
from django.urls import path,include


urlpatterns = [
    
    path ('admin/', admin.site.urls),
    path ('',views.index,name='index'),
]
urlpatterns = [
    
    path ('admin/', admin.site.urls),
    path ('',views.view_cabanas,name='cabanas'),

]
urlpatterns = [
    
    path ('admin/', admin.site.urls),
    path ('',views.confirma_borrar,name='confirma_borrar'),
]
urlpatterns = [
    
    path ('admin/', admin.site.urls),
    path ('',views.formulario,name='formulario'),
]
urlpatterns = [
    
    path ('admin/', admin.site.urls),
    path ('',views.lista,name='lista'),
]