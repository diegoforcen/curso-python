import json
from pathlib import Path

def guardar_json(ruta: Path, datos: dict) -> None:
    """Guarda un diccionario como JSON."""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_json(ruta: Path) -> dict:
    """Lee un archivo JSON y devuelve un diccionario."""
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    ruta = Path("src/config.json")
    config = {"usuario": "Diego", "rol": "Director de IT", "activo": True}
    guardar_json(ruta,config)
    data = cargar_json(ruta)
    print("Configuracion cargada:", data)

