def crear_empleado(nombre: str, edad: int, puesto: str) -> dict:
    return {"nombre": nombre, "edad": edad, "puesto": puesto}

def promedio_edad(empleados: list[dict]) -> float:
    total = sum(e["edad"] for e in empleados)
    return total / len(empleados)

if __name__ == "__main__":
    empleados = [
        crear_empleado("Ana", 30, "Desarrolladora"),
        crear_empleado("Luis", 35, "Analista"),
        crear_empleado("Diego", 43, "Director IT"),
    ]

    print("Lista de empleados:")
    for e in empleados:
        print(e)

    print("Promedio de edad:", promedio_edad(empleados))