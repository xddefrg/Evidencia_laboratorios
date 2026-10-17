"""Validaciones del cotizador."""

import math


def precio_valido(precio):
    return math.isfinite(precio) and precio > 0


def cantidad_valida(cantidad):
    return cantidad > 0


def porcentaje_valido(porcentaje):
    return math.isfinite(porcentaje) and 0 <= porcentaje <= 100
