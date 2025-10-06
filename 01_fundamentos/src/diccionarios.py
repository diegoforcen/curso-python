def demo_diccionarios():
    persona = {
        "nombre": "Diego",
        "edad": "43",
        "ciudad": "Madrid"
    }

    print("Diccionario:", persona)
    print("Nombre:", persona["nombre"])

    persona["profesion"] = "Director IT"
    print("Después de añadir 'profesion':", persona)

    for clave, valor in persona.items():
        print(f"{clave} -> {valor}")

if __name__ == "__main__":
    demo_diccionarios()
    
