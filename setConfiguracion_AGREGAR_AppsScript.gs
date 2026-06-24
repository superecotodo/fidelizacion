// ═══════════════════════════════════════════════════════════════
//  Super ECO todo — Fragmento para GUARDAR el mínimo de canje en la nube
//
//  Pegá esto en el Apps Script de tu hoja de FIDELIZACIÓN
//  (la que tiene Clientes / Movimientos / Configuracion / Empleados),
//  NO en la del catálogo.
//
//  CÓMO INSTALAR:
//  1. Abrí tu Google Sheet de fidelización
//  2. Extensiones → Apps Script
//  3a. Dentro de tu función doPost(e) que YA tenés, agregá el bloque
//      marcado como "AGREGAR DENTRO DE doPost".
//  3b. Pegá la función setConfiguracion (abajo de todo) al final del archivo.
//  4. Guardá (Ctrl+S)
//  5. Implementar → Administrar implementaciones → editá la existente →
//     Versión: "Nueva versión" → Implementar. (Así se actualiza la misma URL.)
// ═══════════════════════════════════════════════════════════════


// ───── AGREGAR DENTRO DE doPost(e), junto a tus otras acciones ─────
// (Tu doPost ya hace algo como: var data = JSON.parse(e.postData.contents);
//  y compara data.action. Sumá esta condición.)

  if (data.action === 'setConfiguracion') {
    return setConfiguracion(data.clave, data.valor);
  }


// ───── PEGAR ESTA FUNCIÓN COMPLETA AL FINAL DEL ARCHIVO ─────
function setConfiguracion(clave, valor) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ws = ss.getSheetByName('Configuracion');
  var rows = ws.getDataRange().getValues();

  for (var i = 0; i < rows.length; i++) {
    if (String(rows[i][0]).trim() === String(clave).trim()) {
      ws.getRange(i + 1, 2).setValue(valor); // columna B = "valor"
      return ContentService
        .createTextOutput(JSON.stringify({ ok: true, clave: clave, valor: valor }))
        .setMimeType(ContentService.MimeType.JSON);
    }
  }

  return ContentService
    .createTextOutput(JSON.stringify({ error: 'clave no encontrada: ' + clave }))
    .setMimeType(ContentService.MimeType.JSON);
}
