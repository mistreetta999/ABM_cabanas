# cabanas_apps/handlers.py
from django.http import HttpResponse, JsonResponse
class handler:
    """Clase base para manejar las solicitudes HTTP."""

    def handle_request(self, request):
        """Método para manejar la solicitud HTTP."""
        raise NotImplementedError("Este método debe ser implementado por subclases.")
# Ejemplo de handler para la página principal
def pagina_principal(request):
    """ define la vista de la página principal del proyecto """
    return HttpResponse("Bienvenida a la gestión de cabañas")

# Handler para listar reservas
def listar_reservas(request):
    """ define la vista para listar todas las reservas """
    reservas = [
        {"id": 1, "cliente": "Carolina", "cabaña": "Cabaña 1"},
        {"id": 2, "cliente": "Juan", "cabaña": "Cabaña 2"},
    ]
    return JsonResponse(reservas, safe=False)

# Handler para detalle de reserva
def detalle_reserva(request, reserva_id):
    """ define la vista para mostrar el detalle de una reserva """
    return HttpResponse(f"Detalle de la reserva {reserva_id}")

# Handler para crear reserva
def crear_reserva(request, cliente_id, cabana_id):
    """ define la vista para crear una nueva reserva """
    return HttpResponse(
        f"Reserva creada para cliente {cliente_id} en cabaña {cabana_id}"
    )

# Handler para borrar reserva
def borrar_reserva(request, reserva_id):
    """ define la vista para borrar una reserva """
    return HttpResponse(f"Reserva {reserva_id} borrada")
