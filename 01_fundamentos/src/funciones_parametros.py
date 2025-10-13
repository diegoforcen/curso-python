def calcular_precio(base: float, iva: float = 21.0, descuento: float = 0.0) -> float:
    """Calcula el precio final aplicando IVA y descuento."""
    total = base * (1 + iva / 100) * (1 - descuento / 100)
    return round(total, 2)

if __name__ == "__main__":
    print("Precio sin descuento:", calcular_precio(100))
    print("Con descuento del 10%:", calcular_precio(100, descuento=10))
    print("Con IVA 10% y descuento 5%:", calcular_precio(200, iva=10, descuento=5))
    