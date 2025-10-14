from pathlib import Path

def leer_seguro(ruta:Path) -> str:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️ Archivo no encontrado: {ruta}")
        return ""
    except PermissionError:
        print(f"⚠️ Sin permisos para leer: {ruta}")
        return ""
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")
        return ""

if __name__ == "__main__":
    print("Intentando leer un archivo inexistente...")
    texto = leer_seguro(Path("src/inexistente.txt"))
    print("Resultado:", texto)