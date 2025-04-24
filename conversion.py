import os
from PIL import Image

# Rutas de las carpetas de origen y destino
carpeta_origen = 'img_v1'
carpeta_destino = 'img_v3'

# Dimensiones deseadas en píxeles para una imagen de 10 cm x 10 cm a 300 DPI
desired_width = 1181  # Ancho en píxeles
desired_height = 1181  # Alto en píxeles

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Leer y procesar cada imagen en la carpeta de origen
for nombre_archivo in os.listdir(carpeta_origen):
    if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):  # Filtrar solo archivos de imagen
        # Ruta completa del archivo de imagen
        ruta_imagen = os.path.join(carpeta_origen, nombre_archivo)

        # Abrir la imagen
        image = Image.open(ruta_imagen)

        # Redimensionar la imagen para asegurarse de que tiene las dimensiones deseadas
        image = image.resize((desired_width, desired_height))

        # Convertir la imagen a CMYK
        cmyk_image = image.convert('CMYK')

        # Definir el nombre de archivo de salida
        nombre_salida = os.path.splitext(nombre_archivo)[0] + '_cmyk.tiff'
        ruta_salida = os.path.join(carpeta_destino, nombre_salida)

        # Guardar la imagen en formato CMYK con una resolución de 300 DPI
        cmyk_image.save(ruta_salida, dpi=(300, 300))

        print(f'Imagen convertida y guardada: {ruta_salida}')

print('Proceso de conversión completado.')

