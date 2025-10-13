def subtotal(cantidades: list[int], precios: list[float]) -> float:
    """Suma de cantidad * precio para cada línea."""
    return sum(c * p for c, p in zip(cantidades, precios))

def aplicar_iva(total: float, iva: float = 21.0) -> float:
    return total * (1 + iva / 100)

def aplicar_descuento(total: float, descuento: float = 0.0) -> float:
    return total * (1 - descuento / 100)
    