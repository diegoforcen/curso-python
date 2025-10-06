def demo_tuplas():
    punto = (10, 20)
    print("Tupla:", punto)
    print("Coordenada X:", punto[0])
    print("Coordenada Y:", punto[1])

    # Desempaquetado

    x, y = punto
    print(f"x={x}, y={y}")

if __name__ == "__main__":
    demo_tuplas()
