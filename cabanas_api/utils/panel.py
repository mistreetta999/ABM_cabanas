from django.shortcuts import render

from cabanas_api.cabanas.forms import CabanaForm
from cabanas_api.clientes.forms import ClienteForm
from cabanas_api.pagos.forms import PagoForm
from cabanas_api.reservas.forms import ReservaForm


# Vista para la página principal
def pagina_principal(request):
    return render(request, "pagina_principal.html")


# Vista para manejar los formularios
def panel_forms(request):
    cliente_form = ClienteForm()
    reserva_form = ReservaForm()
    cabana_form = CabanaForm()
    pago_form = PagoForm()

    context = {
        "cliente_form": cliente_form,
        "reserva_form": reserva_form,
        "cabana_form": cabana_form,
        "pago_form": pago_form,
    }
    return render(request, "forms_panel.html", context)


# Vista para el chatbot
def panel_chatbot(request):
    return render(request, "chatbot/chatbot_panel.html")
