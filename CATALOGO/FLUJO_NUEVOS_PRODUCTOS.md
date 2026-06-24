# 🛒 Flujo para agregar productos al catálogo (con Claude)

## Tus pasos

1. **Copiá las fotos** a `CATALOGO\fotos\`
2. **Avisale a Claude**: "agregué fotos nuevas"
3. Claude crea las filas en la planilla → **abrí el Excel, poné los puntos** y cambiá Activo a **SI** en los que quieras publicar
4. **Guardá y CERRÁ el Excel** (importante: cerrarlo del todo)
5. **Avisale a Claude**: "listo, publicá"

## Lo que hace Claude automáticamente

- Detecta las fotos nuevas comparando con la planilla
- Agrega las filas a `catalogo_plantilla.xlsx` (sin puntos, Activo NO)
- Cuando avisás "listo": lee los puntos, actualiza el catálogo embebido en `CATALOGO/index.html` y `productos.json`
- Verifica integridad de todos los archivos (fotos válidas, HTML completo)
- Hace commit y push a GitHub → la página se actualiza sola en 1-2 minutos

## Notas

- Lo que tenga **NO** en la columna Activo no se publica
- La página web usa los datos embebidos en `index.html`, no `productos.json`
- Página publicada: https://superecotodo.github.io/fidelizacion/CATALOGO/
