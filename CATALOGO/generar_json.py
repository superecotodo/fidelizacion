# ═══════════════════════════════════════════════════════
#  Super ECO todo — Generador de productos.json
#  Ejecutar: python generar_json.py
#  Resultado: genera productos.json en esta misma carpeta
# ═══════════════════════════════════════════════════════

import json
import os

try:
    import openpyxl
except ImportError:
    print("❌ Falta instalar openpyxl. Ejecutá: pip install openpyxl")
    input("Presioná Enter para cerrar...")
    exit()

CARPETA   = os.path.dirname(os.path.abspath(__file__))
EXCEL     = os.path.join(CARPETA, 'catalogo_plantilla.xlsx')
JSON_OUT  = os.path.join(CARPETA, 'productos.json')
URL_BASE_GITHUB = 'https://superecotodo.github.io/catalogo/fotos/'
URL_BASE_DRIVE  = ''  # si usás Drive, pegá el prefijo acá (opcional)

def main():
    if not os.path.exists(EXCEL):
        print(f"❌ No encontré el archivo: {EXCEL}")
        input("Presioná Enter para cerrar...")
        return

    wb   = openpyxl.load_workbook(EXCEL, data_only=True)
    ws   = wb.active
    rows = list(ws.iter_rows(values_only=True))

    # Fila 1 = título decorativo, Fila 2 = encabezados, Fila 3+ = datos
    productos = []
    for fila in rows[2:]:
        id_prod = str(fila[0] or '').strip()
        nombre  = str(fila[1] or '').strip()
        desc    = str(fila[2] or '').strip()
        puntos  = fila[3]
        cat     = str(fila[4] or '').strip()
        foto    = str(fila[5] or '').strip()
        activo  = str(fila[6] or 'SI').strip().upper()

        # Saltar filas vacías, notas y productos inactivos
        if not id_prod or not id_prod.startswith('PRD'):
            continue
        if activo == 'NO':
            continue

        # Resolver URL de la foto
        foto_url = ''
        if foto:
            if foto.startswith('http'):
                # URL completa (Drive u otro)
                foto_url = foto
            else:
                # Nombre de archivo → apunta a GitHub
                foto_url = URL_BASE_GITHUB + foto

        try:
            pts = int(float(puntos)) if puntos else 0
        except:
            pts = 0

        productos.append({
            'id':          id_prod,
            'nombre':      nombre,
            'descripcion': desc,
            'puntos':      pts,
            'categoria':   cat,
            'foto_url':    foto_url,
        })

    # Guardar JSON
    with open(JSON_OUT, 'w', encoding='utf-8') as f:
        json.dump(productos, f, ensure_ascii=False, indent=2)

    print(f"✅ productos.json generado con {len(productos)} productos")
    print(f"📄 Guardado en: {JSON_OUT}")
    print()
    print("📤 Próximo paso: subí a GitHub estos archivos:")
    print("   - productos.json")
    print("   - las fotos nuevas de la carpeta fotos\\")
    input("\nPresioná Enter para cerrar...")

if __name__ == '__main__':
    main()
