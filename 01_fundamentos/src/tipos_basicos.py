def demo_tipos():
    edad: int = 43
    altura: float = 1.85
    nombre: str = "Diego"
    es_manager: bool = True

    print("Edad:", edad, type(edad))
    print("Altura:", altura, type(altura))
    print("Nombre:", nombre, type(nombre))
    print("Es manager:", es_manager, type(es_manager))

    print("Edad como string:", str(edad))
    print("Altura redondeada a int:", int(altura))


if __name__ == "__main__":
    demo_tipos()
