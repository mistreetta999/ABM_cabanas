from django.urls import path

from chatbot import chatbot_views

app_name = "chatbot"

urlpatterns = [
    path("", chatbot_views.chatbot_view, name="chatbot"),
    path("api/", chatbot_views.chatbot_api, name="chatbot_api"),
]
