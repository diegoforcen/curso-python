from pathlib import Path
from src.archivos_csv import escribir_csv
from src.archivos_json import guardar_json

def exportar_empleados(empleados: list[dict], carpeta: Path) -> None:
    carpeta.mkdir(exist_ok=True)
    escribir_csv(carpeta / "empleados.csv", empleados)
    guardar_json(carpeta / "empleados.json", {"empleados": empleados})