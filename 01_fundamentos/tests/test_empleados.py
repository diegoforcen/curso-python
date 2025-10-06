from src.empleados import crear_empleado, promedio_edad

def test_crear_empleado():
    e = crear_empleado("Ana", 30, "Dev")
    assert e["nombre"] == "Ana"
    assert e["edad"] == 30
    assert e["puesto"] == "Dev"

def test_promedio_edad():
    empleados = [
        {"nombre": "A", "edad": 30, "puesto": "X"},
        {"nombre": "B", "edad": 40, "puesto": "Y"},
    ]
    assert promedio_edad(empleados) == 35
