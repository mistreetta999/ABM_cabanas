"""Funciones auxiliares del proyecto de gestion de cabanas."""

from __future__ import annotations

import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from typing import Any

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.translation import gettext_lazy as _


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
ONLY_DIGITS_RE = re.compile(r"\D+")


def limpiar_texto(valor: Any) -> str:
    """Devuelve texto sin espacios sobrantes."""
    if valor is None:
        return ""
    return str(valor).strip()


def normalizar_dni(valor: Any) -> str:
    """Devuelve el DNI solo con numeros."""
    return ONLY_DIGITS_RE.sub("", limpiar_texto(valor))


def validar_dni(valor: Any, *, obligatorio: bool = True) -> str:
    """Valida un DNI argentino basico y devuelve su version normalizada."""
    dni = normalizar_dni(valor)
    if not dni:
        if obligatorio:
            raise ValidationError(_("El DNI es obligatorio."))
        return ""
    if not dni.isdigit():
        raise ValidationError(_("El DNI solo puede contener numeros."))
    if len(dni) < 7 or len(dni) > 9:
        raise ValidationError(_("El DNI debe tener entre 7 y 9 digitos."))
    return dni


def normalizar_telefono(valor: Any) -> str:
    """Devuelve un telefono simple, preservando el signo + inicial."""
    telefono = limpiar_texto(valor)
    if not telefono:
        return ""
    prefijo = "+" if telefono.startswith("+") else ""
    numeros = ONLY_DIGITS_RE.sub("", telefono)
    return f"{prefijo}{numeros}"


def validar_telefono(valor: Any, *, obligatorio: bool = False) -> str:
    """Valida un telefono y devuelve su version normalizada."""
    telefono = normalizar_telefono(valor)
    if not telefono:
        if obligatorio:
            raise ValidationError(_("El telefono es obligatorio."))
        return ""
    digitos = telefono[1:] if telefono.startswith("+") else telefono
    if len(digitos) < 6 or len(digitos) > 15:
        raise ValidationError(_("El telefono debe tener entre 6 y 15 digitos."))
    return telefono


def validar_email(valor: Any, *, obligatorio: bool = False) -> str:
    """Valida un email y lo devuelve en minusculas."""
    email = limpiar_texto(valor).lower()
    if not email:
        if obligatorio:
            raise ValidationError(_("El email es obligatorio."))
        return ""
    if not EMAIL_RE.match(email):
        raise ValidationError(_("Ingrese un email valido."))
    return email


def convertir_fecha(valor: Any, nombre_campo: str = "fecha") -> date:
    """Convierte date, datetime o texto YYYY-MM-DD en date."""
    if isinstance(valor, datetime):
        return timezone.localtime(valor).date() if timezone.is_aware(valor) else valor.date()
    if isinstance(valor, date):
        return valor
    fecha = parse_date(limpiar_texto(valor))
    if fecha is None:
        raise ValidationError({nombre_campo: _("Ingrese una fecha valida.")})
    return fecha


def validar_rango_fechas(
    fecha_inicio: Any,
    fecha_fin: Any,
    *,
    campo_inicio: str = "fecha_inicio",
    campo_fin: str = "fecha_fin",
) -> tuple[date, date]:
    """Valida que la fecha de salida sea posterior a la de llegada."""
    inicio = convertir_fecha(fecha_inicio, campo_inicio)
    fin = convertir_fecha(fecha_fin, campo_fin)
    return inicio, fin


def calcular_noches(fecha_inicio: Any, fecha_fin: Any) -> int:
    """Calcula la cantidad de noches entre dos fechas validas."""
    inicio, fin = validar_rango_fechas(fecha_inicio, fecha_fin)
    return (fin - inicio).days


def validar_monto(valor: Any, *, campo: str = "monto") -> Decimal:
    """Valida importes positivos para pagos, reservas o alquileres."""
    try:
        monto = Decimal(str(valor))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValidationError({campo: _("Ingrese un monto valido.")}) from exc
    if monto <= 0:
        raise ValidationError({campo: _("El monto debe ser mayor a cero.")})
    return monto


def esta_ocupado_en_rango(queryset: Any, fecha_inicio: Any, fecha_fin: Any) -> bool:
    """Comprueba superposicion de fechas en un queryset de reservas/alquileres."""
    inicio, fin = validar_rango_fechas(fecha_inicio, fecha_fin)
    return queryset.filter(fecha_inicio__lt=fin, fecha_fin__gt=inicio).exists()
