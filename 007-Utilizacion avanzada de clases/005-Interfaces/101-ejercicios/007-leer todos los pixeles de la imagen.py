from PIL import Image

imagen = Image.open("foto curriculum.jpeg")

anchura,altura = imagen.size                         # Cojo altura y anchura


for x in range(0,anchura):                           # Repaso la anchura
    for y in range(0,altura):                        # Repaso la altura

        pixel1 = imagen.getpixel((0, 0))             # Cojo cada pixel
        print(pixel1)                                # Lo saco por pantalla
 