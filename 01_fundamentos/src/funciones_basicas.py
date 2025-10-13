def saludar (nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}! Bienvenido a Python."

if __name__ == "__main__":
    mensaje = saludar("Diego")
    print(mensaje)
