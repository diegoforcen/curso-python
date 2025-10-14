from pathlib import Path
from exportar_empleados import exportar_empleados
import json, csv

def test_exportar(tmp_path: Path):
    empleados = [
        {"nombre": "Ana", "edad": 30},
        {"nombre": "Luis", "edad": 40},
    ]
    exportar_empleados(empleados, tmp_path)

    # Verificar CSV
    csv_path = tmp_path / "empleados.csv"
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        filas = list(reader)
        assert len(filas) == 2

    # Verificar JSON
    json_path = tmp_path / "empleados.json"
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
        assert len(data["empleados"]) == 2
