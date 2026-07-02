from django.shortcuts import render

def pagina_principal(request):
    """
    Vista principal de gestión de cabañas.
    Se conecta con la interfaz y permite acceder a las demás apps.
    """
    return render(request, "gestion_cabanas/pagina_principal.html")
