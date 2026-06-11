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

    # Fila 1 = encabezados, Fila 2+ = datos
    # Columnas: ID | Nombre | Descripcion | Puntos | Categoria | Codigo_Barra | Imagen | Foto_URL | Activo
    productos = []
    for fila in rows[1:]:
        id_prod = str(fila[0] or '').strip()
        nombre  = str(fila[1] or '').strip()
        desc    = str(fila[2] or '').strip()
        puntos  = fila[3]
        cat     = str(fila[4] or '').strip()
        imagen  = str(fila[6] or '').strip()
        url_ext = str(fila[7] or '').strip()
        activo  = str(fila[8] or 'NO').strip().upper()

        # Saltar filas vacías, notas y productos inactivos
        if not id_prod or not id_prod.startswith('PRD'):
            continue
        if activo != 'SI':
            continue

        # Resolver URL de la foto: Foto_URL completa > archivo local en fotos/
        foto_url = ''
        if url_ext.startswith('http'):
            foto_url = url_ext
        elif imagen:
            foto_url = 'fotos/' + imagen

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
