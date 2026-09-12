""""Vistas para la aplicación del chatbot."""
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def panel_chatbot(request):
    """ panel"""
    return render(request, "chatbot/panel.html")

def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return JsonResponse({
        "id": reserva.id,
        "cliente": reserva.cliente.nombre,
        "cabana": reserva.cabana.nombre,
        "fecha_ingreso": reserva.fecha_ingreso,
        "fecha_salida": reserva.fecha_salida,
    })

def panel_chatbot(request):
    """
    Vista que muestra el panel del chatbot.
    """
    context = {
        "titulo": "Panel del Chatbot",
        "descripcion": "Aquí podés interactuar con el chatbot de Cabañas."
    }
    return render(request, "chatbot/panel.html", context)

def chatbot_panel(request):
    """Renderiza el panel del chatbot."""
    return render(request, "chatbot/panel_chatbot.html")

def chatbot_view(request):
    """Renderiza la interfaz principal del chatbot."""
    return render(request, "chatbot/chatbot.html")

def panel_chatbot_respuestas(request):
    """
    Vista que muestra el panel del chatbot.
    """
    context = {
        "titulo": "Panel del Chatbot",
        "descripcion": "Aquí podés interactuar con el chatbot de Cabañas."
    }
    return render(request, "chatbot/panel.html", context)
