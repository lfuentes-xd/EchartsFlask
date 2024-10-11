# Usar una imagen base oficial de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /main

# Copiar los archivos de tu proyecto al directorio de trabajo
COPY . /main

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r Requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
