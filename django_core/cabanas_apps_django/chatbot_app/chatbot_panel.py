from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .chatbot import ChatBot

bot = ChatBot()


class ChatbotPanel:
    """views chatbot"""

    def chatbot_panel(self, request: HttpRequest) -> HttpResponse:
        """Renderiza la página del panel del chatbot."""
        if request.method == "POST":
            user_message = request.POST.get("message", "")
            response = bot.respond(user_message)
            return render(request, "chatbot/panel.html", {"response": response})
        return render(request, "chatbot/panel.html", {"response": bot.welcome_message})


def chatbot_panel(request: HttpRequest) -> HttpResponse:
    """Renderiza el panel del chatbot."""
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        response = bot.respond(user_message)
        return render(request, "chatbot/panel_chatbot.html", {"response": response})
    return render(
        request, "chatbot/panel_chatbot.html", {"response": bot.welcome_message}
    )
