# Política de seguridad

## Alcance

El repositorio publica agregados, artefactos de paridad y resultados. No contiene datos personales identificables ni los conjuntos de origen de terceros, y el tablero se sirve como archivos estaticos sin backend.



## Cómo reportar

Si encuentras una vulnerabilidad, usa los **avisos privados de seguridad** de
GitHub: pestaña *Security* → *Report a vulnerability*. Evita abrir un *issue*
público con detalles explotables.

Incluye, cuando aplique:

- versión o commit afectado;
- pasos mínimos para reproducir;
- impacto esperado y observable;
- cualquier mitigación que ya hayas probado.

## Buenas prácticas para quien despliega

- No añadas credenciales al repositorio; usa variables de entorno.
- Sirve la demo detrás de HTTPS si la expones fuera de `127.0.0.1`.
- Revisa el resultado de la verificación de credenciales de la integración
  continua antes de fusionar cambios.

Este es un proyecto de portafolio mantenido de forma individual: se revisan los
reportes por orden de llegada y se responde con una evaluación inicial cuando el
reporte contiene pasos reproducibles.
