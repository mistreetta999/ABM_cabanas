from django.shortcuts import render

def panel_principal(request):
    """
    Vista principal de la interfaz de gestión de cabañas.
    Desde aquí se puede acceder a las demás apps: cabañas, reservas, alquileres, pagos, registros y chatbot.
    """
    return render(request, "interfaz_gestion_cabanas/panel.html")
