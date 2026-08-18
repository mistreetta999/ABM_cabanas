# chatbot_home.py
from django.http import HttpResponse

def chatbot_home(request):
    """Renderiza la página de pagina_principal del chatbot."""
    return HttpResponse("Bienvenida Carolina 💙, este es el chatbot funcionando en Django!")
