def calcular_total(cantidad: int, precio_unitario:float) -> float:
    return cantidad * precio_unitario

def aplicar_descuento(total:float, porcentaje: float) -> float:
    return total * (1 - porcentaje / 100)

def generar_factura(cantidad: int, precio_unitario: float, descuento: float = 0.0) -> float:
    subtotal = calcular_total(cantidad, precio_unitario)
    total = aplicar_descuento(subtotal, descuento)
    return round(total,2)

if __name__ == "__main__":
    print("Factura final:", generar_factura(3,50,10))