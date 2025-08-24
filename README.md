# Práctico 2 — CRUD Django (Oficinas / Personas) + Auth + Captcha

Proyecto armadito para que lo levantes rápido. Está comentado en argentino y sin tanta vuelta.

## Qué trae
- Apps separadas: `oficinas`, `personas`, `accounts` (login, logout, registro con captcha)
- CRUD completo con paginación, búsqueda (por nombre de persona), y detalle de oficina mostrando sus personas.
- Carga masiva por CSV para **oficinas** y **personas** (desde interfaz).
- Navbar con Bootstrap 5, links a listas, barra de búsqueda y botón Ingresar/Salir.
- Permisos: crear/editar/eliminar solo logueado.
- Templates responsive con grid de Bootstrap.

## Instalación rápida
```bash
# 1) Crear entorno (en Windows PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# o en Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Crear tablas y preparar captcha
python manage.py migrate

# 4) Crear superusuario para probar
python manage.py createsuperuser

# 5) Levantar el server
python manage.py runserver
```

## Variables clave
- Usuario anónimo: puede ver listados y detalles.
- Usuario logueado: además puede **crear/editar/eliminar** y **cargar CSV**.

## Carga masiva (CSV)
- Oficinas: columnas `nombre,nombre_corto`
- Personas: columnas `apellido,nombre,edad,oficina_nombre_corto`

Ejemplos en `samples/`.

> Nota: si rompés algo, calmate, corré `migrate` y revisá la consola. Los mensajes de error están pensados para entender qué pasó al toque.
