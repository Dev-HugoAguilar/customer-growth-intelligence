# Datos, artefactos y límites

## Conjuntos de origen

| Conjunto | Uso | ¿Se redistribuye aquí? |
|---|---|---|
| **Complete Journey** (Dunnhumby) | Cohorte de hogares, transacciones y campañas; corte activo 2017-09-01 sobre 90 días desde el 3 de junio de 2017. | **No**. Se publican agregados y artefactos derivados. |
| **Criteo Uplift Prediction** | Auditoría de viabilidad y benchmark de *uplift* con muestras de 500 mil y 100 mil filas. | **No**. Se documenta la descarga y el procedimiento. |

Los archivos crudos (`*.csv.gz` de Criteo y las tablas originales de Complete
Journey) no se versionan. `pipeline/src/download_transactions.py` y
`pipeline/src/audit_criteo_uplift.py` documentan la obtención y la validación.

## Qué se publica

- **Artefactos del tablero** (`dashboard-campanas/data/*.json`): perfiles,
  evolución, campañas, incrementalidad, experimento y manifiesto. Son agregados y
  curvas; no contienen identificadores de personas.
- **Artefactos de paridad** (`dashboard-campanas/paridad/`): tablas de contraste
  que permiten reconstruir y verificar cada visualización, con su inventario y sus
  hashes.
- **Resultados del pipeline** (`pipeline/reports/`): validaciones, benchmarks,
  potencia de experimento y decisiones documentadas.

## Unidades que la documentación respeta

- **Hogar comprador del cohorte**: unidad de la segmentación y de la propensión.
  No es una persona física.
- **Campaña en prueba**: unidad del experimento; el análisis es ITT y el
  denominador se declara en cada cifra.
- **Curva de ganancia**: acumulados por fracción contactada; no son una predicción
  de ingresos.
- **Segmento**: etiqueta descriptiva alineada por hogar entre cortes, no un
  diagnóstico causal.

## Decisiones de lectura

- Los porcentajes usan denominadores explícitos y se declaran en el pie de cada
  cifra.
- Las comparaciones múltiples se ajustan con Holm y el ajuste se reporta.
- Una bandera de aleatorización no se acepta como prueba: se exige el manifiesto
  con semilla, estratos y tamaños.
- Los benchmarks de Criteo se repiten con varias semillas; las diferencias entre
  semillas se documentan en lugar de presentar el mejor resultado.

## Límites

- La cohorte es un corte histórico; los patrones no se extrapolan a otro mercado.
- La segmentación describe, no explica.
- La propensión ordena hogares; no cuantifica el efecto de contactarlos. Esa
  pregunta la responde el experimento, y solo bajo sus supuestos.
- El repositorio no incluye datos personales identificables ni permite
  reidentificar hogares.
