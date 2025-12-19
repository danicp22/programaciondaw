from PIL import Image

imagen = Image.open("foto curriculum.jpeg")

pixel1 = imagen.getpixel((0, 0))

print(pixel1)