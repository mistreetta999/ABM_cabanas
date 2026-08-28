""" utils"""
from datetime import date

def calcular_disponibilidad(cabana, fecha_inicio, fecha_fin):
    """
    Verifica si una cabaña está disponible entre dos fechas.
    Retorna True si no hay reservas que se solapen.
    """
    reservas = cabana.reserva_set.filter(
        fecha_inicio__lt=fecha_fin,
        fecha_fin__gt=fecha_inicio
    )
    return not reservas.exists()

def calcular_precio_total(cabana, fecha_inicio, fecha_fin):
    """
    Calcula el precio total de la estadía en base al precio por noche.
    """
    dias = (fecha_fin - fecha_inicio).days
    return dias * cabana.precio

def obtener_cabanas_disponibles(cabanas_queryset, fecha_inicio, fecha_fin):
    """
    Devuelve una lista de cabañas disponibles en el rango de fechas.
    """
    disponibles = []
    for cabana in cabanas_queryset:
        if calcular_disponibilidad(cabana, fecha_inicio, fecha_fin):
            disponibles.append(cabana)
    return disponibles

def generar_codigo_cabana(prefix="CAB"):
    """
    Genera un código único para identificar cada cabaña.
    """
    hoy = date.today()
    return f"{prefix}-{hoy.strftime('%Y%m%d')}"
