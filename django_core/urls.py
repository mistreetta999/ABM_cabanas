from django.contrib import admin
from django.urls import path, include
from django_core.views import chatbot_view
from cabana_apps.views  import index 
from chatbot.chatbot_views import ChatbotViews
from chatbot.chatbot import chatbot
from typing import Any
class urls
    def __init__(self):
        self.urlpatterns = Any
        self.urlpatterns = [
            path("admin/", admin.site.urls),
            path('', index, name='index'),
            path("chatbot/", include("chatbot.urls")), 
            path('reservas/', include('cabana_apps.alquileres_reservas.urls')),# nueva ruta
            path('chatbot/', chatbot_view)   
            # Rutas de las aplicaciones internas
            path("reservas/", include("cabana_apps.reservas.urls")),
            path("clientes/", include("cabana_apps.clientes.urls")),
            path("registros/", include("cabana_apps.registros.urls")),

            # App principal de cabañas
            path("cabanas/", include("cabanas.urls")),
            path("reservas/", include("cabana_apps.reservas.urls")),

            ]
urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path("chatbot/", include("chatbot.urls")), 
    path('reservas/', include('cabana_apps.alquileres_reservas.urls')),# nueva ruta
    path('chatbot/', chatbotview)   
    # Rutas de las aplicaciones internas
    path("reservas/", include("cabana_apps.reservas.urls")),
    path("clientes/", include("cabana_apps.clientes.urls")),
    path("registros/", include("cabana_apps.registros.urls")),

    # App principal de cabañas
    path("cabanas/", include("cabanas.urls")),
    path("reservas/", include("cabana_apps.reservas.urls")),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),  # nueva ruta
]

urlpatterns = [
    path('', chatbot_view, name='chatbot'),
]
