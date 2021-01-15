pip install Pillow


Piloww ==  8.1.0
from PIL import Image
import sys
try:
    img = Image.open("gato.jpg")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)
img.show()# mostrar imagen

img.save("gato.png","png")#conversión de JPG a PNG

img2 = img.rotate(45)#Rotación de imágenes
img2.show() #Mostrar la imagen

ancho,alto = img.size#Encontrar ancho y alto de una imagen
print("Ancho: ",ancho)
print("Alto: ",alto)

size = (200,200)#Reescalar imágenes y crear thumbnails
img3 = img.resize(size)
img4 = img.copy()
img4.thumbnail(size)
img3.show()
img4.show()

pixels = img.load()#Averiguar los colores de un pixel
clr = pixels[10,10]
print(clr)