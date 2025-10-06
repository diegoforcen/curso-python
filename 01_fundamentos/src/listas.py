def demo_listas():
    numeros = [10, 20, 30]
    print("Lista original:", numeros)

    #Añadir elementos
    numeros.append(40)
    print("Después de append:", numeros)

    #Quitar el último
    numeros.pop()
    print("Después de pop:", numeros)

    #Insertar en posición concreta
    numeros.insert(1, 15)
    print("Después de insert:", numeros)

    #Recorremos la lista
    for n in numeros:
        print("Elemento:", n)

    #Comprensión de listas (formas compacta)

    cuadrados = [n ** 2 for n in numeros]
    print("Cuadrados:", cuadrados)

if __name__ == "__main__":
    demo_listas()
