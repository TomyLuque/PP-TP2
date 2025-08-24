# practico 2 — CRUD Django (oficinas/ personas) auth, captcha



## el proyecto:
- apps separadas: `oficinas`, `personas`, `accounts` (login, logout, registro con captcha)
- CRUD completo con paginacion, busqueda  y detalle de oficina mostrando sus personas.
- carga masiva por CSV
- navbar con Bootstrap 5, links a listas, barra de búsqueda y botón ingresar/Salir
- Permisos: crear/editar/eliminar solo logueado.
- templates responsive con grid de Bootstrap

## instalacion
```bash
# 1) crear entorno
python -m venv .venv
.\.venv\Scripts\Activate.ps1


# 2) instalar dependencias
pip install -r requirements.txt

# 3) crear tablas y preparar captcha
python manage.py migrate

# 4) crear superusuario para probar
python manage.py createsuperuser

# 5) levantar el server
python manage.py runserver
```

## variables clave
- usuario anónimo: puede ver listados y detalles.
- usuario logueado: ademas puede **crear/editar/eliminar** y **cargar CSV**.

## carga masiva (CSV)
- oficinas: columnas `nombre,nombre_corto`
- personas: columnas `apellido,nombre,edad,oficina_nombre_corto`


