from facturacion.operaciones import subtotal, aplicar_iva, aplicar_descuento

def generar_factura(cantidades: list[int], precios: list[float], iva: float = 21.0, descuento: float = 0.0) -> float:
    sub = subtotal(cantidades, precios)
    con_descuento = aplicar_descuento(sub, descuento)
    total = aplicar_iva(con_descuento, iva)
    return round(total, 2)