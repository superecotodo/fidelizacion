// ═══════════════════════════════════════════════════════════════
//  Super ECO todo — Apps Script para Catálogo de Canjes
//  Columnas del Google Sheet (en orden):
//  A: ID | B: Nombre | C: Descripcion | D: Puntos | E: Categoria
//  F: Codigo_Barra | G: Imagen | H: Foto_URL | I: Activo
//
//  CÓMO INSTALAR:
//  1. Abrí tu Google Sheet del catálogo
//  2. Extensiones → Apps Script
//  3. Borrá todo el código que aparece y pegá este
//  4. Guardá (Ctrl+S)
//  5. Clic en "Implementar" → "Nueva implementación"
//  6. Tipo: Aplicación web
//     Ejecutar como: Yo
//     Quién tiene acceso: Cualquier persona
//  7. Clic en "Implementar" → copiá la URL que aparece
//  8. Pegá esa URL en index.html donde dice APPS_SCRIPT_URL
// ═══════════════════════════════════════════════════════════════

// URL base de GitHub Pages donde están las fotos
const BASE_FOTOS = 'https://superecotodo.github.io/fidelizacion/CATALOGO/fotos/';

function doGet(e) {
  try {
    const ss   = SpreadsheetApp.getActiveSpreadsheet();
    const ws   = ss.getActiveSheet();
    const rows = ws.getDataRange().getValues();

    // Fila 0 = encabezados, Fila 1 en adelante = productos
    const productos = [];

    for (let i = 1; i < rows.length; i++) {
      const fila = rows[i];

      const id          = String(fila[0] || '').trim();
      const nombre      = String(fila[1] || '').trim();
      const descripcion = String(fila[2] || '').trim();
      const puntos      = parseInt(fila[3]) || 0;
      const categoria   = String(fila[4] || '').trim();
      // fila[5] = Codigo_Barra (no se envía al frontend)
      const imagen      = String(fila[6] || '').trim();
      const foto_manual = String(fila[7] || '').trim();
      const activo      = String(fila[8] || 'SI').trim().toUpperCase();

      // Saltar filas vacías o inactivas
      if (!id || !id.startsWith('PRD')) continue;
      if (activo === 'NO') continue;
      if (!nombre || puntos <= 0) continue;

      // Si hay Foto_URL manual la usa; si no, arma la URL desde el nombre de imagen
      const foto_url = foto_manual || (imagen ? BASE_FOTOS + imagen : '');

      productos.push({
        id:          id,
        nombre:      nombre,
        descripcion: descripcion,
        puntos:      puntos,
        categoria:   categoria,
        foto_url:    foto_url
      });
    }

    const output = ContentService.createTextOutput(JSON.stringify(productos));
    output.setMimeType(ContentService.MimeType.JSON);
    return output;

  } catch(err) {
    const output = ContentService.createTextOutput(JSON.stringify({ error: err.message }));
    output.setMimeType(ContentService.MimeType.JSON);
    return output;
  }
}
