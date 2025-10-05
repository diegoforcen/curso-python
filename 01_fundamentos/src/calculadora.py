def leer_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Debes introducir un número válido.")


def leer_op() -> str:
    ops = {"+", "-", "*", "/"}
    while True:
        op = input("Operacion (+ - * /): ").strip()
        if op in ops:
            return op
        print("Error: Operacion no válida.")


def calcular(a: float, b: float, op: str) -> float:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return a / b
    raise ValueError("Operacion desconocida.")


if __name__ == "__main__":
    a = leer_float("Introduce el primer número: ")
    b = leer_float("Introduce el segundo número: ")
    op = leer_op()
    try:
        res = calcular(a, b, op)
        print(f"Resultado: {res:.2f}")
    except ZeroDivisionError as e:
        print(f"Error{e}")
