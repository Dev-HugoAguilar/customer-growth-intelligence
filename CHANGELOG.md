# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
las versiones usan [Versionado Semántico](https://semver.org/lang/es/).

## [1.0.0] — 2026-11-26

### Añadido

- Primera publicación consolidada. Reúne tres piezas antes separadas del
  portafolio: `marketing_customer_project`, `clientes-campanas` y
  `clientes-en-movimiento`.
- Pipeline analítico con propensión de respuesta, validación robusta entre cortes,
  segmentación K-Means alineada por hogar, plan y aleatorización de experimentos,
  análisis ITT con corrección de Holm, referencia de *uplift* y auditoría del
  dataset Criteo.
- Tablero integrado de clientes y campañas, publicado con sus artefactos y sus
  tablas de paridad.
- Tablero semanal publicado sobre la misma capa de datos.
- **18 pruebas** de artefactos y de plantillas, incluidas las guardas del
  aleatorizador y del analizador ITT.
- Documentación de metodología, proyecto integrado, datos y límites.
- Integración continua de pruebas, sintaxis, integridad y credenciales.

### Nota

Los conjuntos de origen (Complete Journey y Criteo) no se redistribuyen. El
constructor del tablero se conserva en el monorepo de origen porque su verificación
de paridad byte a byte está atada a ese layout.
