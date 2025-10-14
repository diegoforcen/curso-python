import csv
from pathlib import Path

def escribir_csv(ruta: Path, filas: list[dict]) -> None:
    """Escribe una lista de diccionarios en un CSV."""
    if not filas:
        return
    campos = filas[0].keys()
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)

def leer_csv(ruta:Path) -> list[dict]:
    """Lee un CSV y devuelve una lista de diccionarios."""
    with open(ruta, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)

if __name__ == "__main__":
    ruta = Path("src/empleados.csv")
    empleados = [
        {"nombre": "Ana", "edad": "30", "puesto": "Dev"},
        {"nombre": "Diego", "edad": "43", "puesto": "IT Manager"},
    ]
    escribir_csv(ruta, empleados)
    datos = leer_csv(ruta)
    print("Datos leidos:")
    print(datos)
    