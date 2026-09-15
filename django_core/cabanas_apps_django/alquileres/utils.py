"""utils"""

from datetime import date, datetime, timedelta

hoy = date.today()
nueva_fecha = hoy + timedelta(days=5)


def calcular_dias_alquiler(fecha_inicio, fecha_fin):
    """Devuelve la cantidad de días entre dos fechas."""
    return (fecha_fin - fecha_inicio).days


def calcular_precio_total(dias, precio_por_dia):
    """Calcula el precio total del alquiler."""
    return dias * precio_por_dia


def generar_codigo_alquiler(prefix="ALQ"):
    """Genera un código único para alquileres."""
    ahora = datetime.now()
    return f"{prefix}-{ahora.strftime('%Y%m%d%H%M%S')}"
