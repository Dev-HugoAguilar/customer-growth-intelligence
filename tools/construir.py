"""Construye el tablero integrado a partir de los artefactos de paridad.

Recuperado del paquete de entrega original (`tools/build.py`) y adaptado a este
repositorio: lee las tablas de `dashboard-campanas/paridad/`, la plantilla y los
scripts de `dashboard-campanas/src/`, y escribe `dashboard-campanas/app/index.html`
junto con `build/sha256.json` (no sobrescribe el de paridad).

    python tools/construir.py
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARIDAD = ROOT / "dashboard-campanas" / "paridad"
SRC = ROOT / "dashboard-campanas" / "src"
SALIDA = ROOT / "dashboard-campanas" / "app" / "index.html"

TABLAS = {
    "hogares": "02c2_hogares_datos_reales.csv",
    "segmentos": "02a2_medianas_datos_reales.csv",
    "cuantiles": "02b2_cuantiles_datos_reales.csv",
    "departamentos": "02d2_departamentos_datos_reales.csv",
    "k": "02e_diagnostico_k_datos_reales.csv",
    "flujos": "03a2_transiciones_datos_reales.csv",
    "estabilidad": "03b_estabilidad_datos_reales.csv",
    "metricas": "04a2_metricas_datos_reales.csv",
    "targeting": "04b_targeting_datos_reales.csv",
    "calibracion": "04c_calibracion_datos_reales.csv",
    "campanas": "04d_campanas_datos_reales.csv",
    "carreras": "05b2_carreras_datos_reales.csv",
    "resumen": "05b3_resumen_datos_reales.csv",
    "uplift": "05c_curvas_datos_reales.csv",
    "rangos": "05d2_rangos_datos_reales.csv",
    "escenarios": "06d_escenarios_datos_reales.csv",
    "capacidad": "06e_capacidad_datos_reales.csv",
}
NARRATIVAS = {
    "proyecto_kpis": "01_indicadores.csv",
    "artefactos": "01f_artefactos.csv",
    "criteo_contexto": "05a_contexto_criteo.csv",
    "inventario": "inventario_visualizaciones.csv",
    "perfil_otro_corte": "02a_indicadores_tamano_otro_corte.csv",
    "procedencia": "procedencia_analisis.csv",
}


def leer(nombre: str) -> list[dict[str, str]]:
    return list(csv.DictReader((PARIDAD / nombre).open(encoding="utf-8-sig")))


def main() -> int:
    faltantes = [n for n in list(TABLAS.values()) + list(NARRATIVAS.values()) if not (PARIDAD / n).exists()]
    if faltantes:
        print("ERROR: faltan artefactos de paridad:")
        for nombre in faltantes:
            print(f"  - {nombre}")
        return 1

    data = {clave: leer(archivo) for clave, archivo in {**TABLAS, **NARRATIVAS}.items()}
    data["fuentes"] = {**TABLAS, **NARRATIVAS}
    data["manifiesto"] = json.loads((PARIDAD / "00_manifiesto_artefactos.json").read_text(encoding="utf-8-sig"))

    crudo = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    css = (SRC / "styles.css").read_text(encoding="utf-8") + "\n" + (SRC / "integracion.css").read_text(encoding="utf-8")
    js = "\n".join(
        (SRC / nombre).read_text(encoding="utf-8")
        for nombre in ("app.js", "integracion.js", "laboratorio.js")
    )
    html = (
        (SRC / "template.html").read_text(encoding="utf-8")
        .replace("__CSS__", css)
        .replace("__DATA__", crudo)
        .replace("__JS__", js)
    )

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(html, encoding="utf-8")
    manifiesto = {v: hashlib.sha256((PARIDAD / v).read_bytes()).hexdigest() for v in {**TABLAS, **NARRATIVAS}.values()}
    destino = ROOT / "dashboard-campanas" / "build" / "sha256.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(manifiesto, indent=2), encoding="utf-8")

    print(f"OK: {SALIDA.relative_to(ROOT)} · {len(html.encode('utf-8')):,} bytes · {len(data['hogares'])} hogares")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

