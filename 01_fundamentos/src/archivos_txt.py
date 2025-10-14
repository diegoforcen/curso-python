from pathlib import Path

def escribir_archivo(ruta: Path, texto: str) -> None:
    """Escribe texto en un archivo (sobrescribe si existe)."""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)

def leer_archivo(ruta:Path) -> str:
    """Lee el contenido completo de un archivo."""
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

if __name__=="__main__":
    ruta = Path("src/saludo.txt")
    escribir_archivo(ruta, "Hola Diego 👋\nBienvenido al módulo 5.")
    contenido = leer_archivo(ruta)
    print("Contenido del archivo:")
    print(contenido)
