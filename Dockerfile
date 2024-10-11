# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al directorio de trabajo
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
