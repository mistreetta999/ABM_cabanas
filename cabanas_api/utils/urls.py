from django.urls import path

from cabanas_api.utils import panel

urlpatterns = [
    # Página principal
    path("", panel.pagina_principal, name="pagina_principal"),
    # Panel de formularios
    path("forms/", panel.panel_forms, name="panel_forms"),
    # Panel del chatbot
    path("chatbot/", panel.panel_chatbot, name="panel_chatbot"),
]
