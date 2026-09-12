""" administración de modelos en el panel de administración de Django."""
from django.contrib import admin

try:
    from clientes.models import Cliente, ClienteDatos  # type: ignore
except ImportError:
    Cliente = None
    ClienteDatos = None

try:
    from reservas.models import Reserva  # type: ignore
except ImportError:
    Reserva = None

try:
    from pagos.models import Pago  # type: ignore
except ImportError:
    Pago = None

try:
    from cabanas.models import Cabana  # type: ignore
except ImportError:
    Cabana = None

# Registro de modelos en el admin
if Cliente is not None:
    admin.site.register(Cliente)
if ClienteDatos is not None:
    admin.site.register(ClienteDatos)
if Reserva is not None:
    admin.site.register(Reserva)
if Cabana is not None:
    admin.site.register(Cabana)
if Pago is not None:
    admin.site.register(Pago)
