# cabanas_apps/interfaz_gestion_cabanas/handles.py

from .views import (
    Cabanas
,
    Alquileres,
    Usuarios,
    Reservas,
    Pagos,
    Registros,
    Chatbot,
    Clientes,
)

# Centralizamos las vistas en un diccionario
def render_unified_panel():
    return {
        "Cabanas
": Cabanas
,
        "Alquileres": Alquileres,
        "Usuarios": Usuarios,
        "Reservas": Reservas,
        "Pagos": Pagos,
        "Registros": Registros,
        "Chatbot": Chatbot,
        "Clientes": Clientes,
    }
