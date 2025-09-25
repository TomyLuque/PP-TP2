# Imagen base de Python
FROM python:3.10-slim

# Variables de entorno para que Python no guarde caché y loguee directo
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar requirements y luego instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/

# Exponer el puerto donde corre Django
EXPOSE 8000

# Comando por defecto: ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
