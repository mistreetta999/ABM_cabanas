import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def chatbot_page(request):
    return render(request, 'chatbot/chatbot.html')


@csrf_exempt
def chatbot_api(request):
    if request.method != 'POST':
        return JsonResponse({'reply': 'Envia una consulta para recibir informacion.'})

    data = json.loads(request.body or '{}')
    message = data.get('message', '').lower()
    if 'precio' in message or 'tarifa' in message:
        reply = 'Las tarifas dependen de la cantidad de huespedes y fechas. Podes dejar tus datos en reservas.'
    elif 'ubicacion' in message or 'donde' in message:
        reply = 'Estamos en Mina Clavero, Cordoba, cerca del centro y de los balnearios principales.'
    else:
        reply = 'Gracias por consultar. Para reservar, comunicate por WhatsApp o carga una reserva en el ABM.'
    return JsonResponse({'reply': reply})
