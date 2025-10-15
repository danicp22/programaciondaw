'''
Programa calculador de IVA
v0.1 Daniel Calve Pardo 2025
Este programa calcula el precio total con IVA y dice si el producto esta disponible en stock
'''

#Declaramos el valor de IVA
IVA = 0.21


#Pedimos datos
nombre_producto = input("Introducta el nombre del producto:")
precio_base = int(input("Introduce el precio del producto:"))
stock = int(input("Introduce el stock de tu producto:"))

if stock == 0:
    print("No quedan unidades")
    exit() 
elif stock <= 5:
    print("Quedan pocas unidades")
else:
    print("El producto está disponible")

    
    
#Calculos
total_iva = precio_base * IVA
precio_total = precio_base + total_iva


#Mostrar en pantalla
print("Producto:",nombre_producto)
print("Precio (Sin IVA):",precio_base,"€")
print("Stock:",stock)
print("IVA (21%):",total_iva,"€")
print("Precio total:",precio_total,"€")
