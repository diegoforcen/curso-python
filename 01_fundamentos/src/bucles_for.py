def cuadrados(n:int) -> list[int]:
    """Devuelve una lista con los cuadrados de 0 a n-1"""
    resultado = []
    for i in range(n):
        resultado.append(i * i)
    return resultado

if __name__ == "__main__":
    print("Cuadrados hasta 10:", cuadrados(10))
