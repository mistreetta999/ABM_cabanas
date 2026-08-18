"""
Archivo includ.py
Centraliza imports de la app django_core
"""

# Importar vistas
from cabanas_apps.cabanas import views as cabanas_views
from cabanas_apps.chatbot_app import views as chatbot_views
from cabanas_apps.reservas import views as reservas_views

# Importar modelos
from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.clientes.models import Cliente
from cabanas_apps.reservas.models import Reserva
from cabanas_apps.pagos.models import Pago

# Importar utilidades si existen
try:
    from cabanas_apps.chatbot_app import chatbot_panel
except ImportError:
    chatbot_panel = None
