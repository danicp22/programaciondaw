- El objetivo de este ejercicio es desarrollar un programa en Python que permita registrar información básica de un producto, como su nombre, precio y cantidad en stock. Además, se busca calcular el precio con IVA (21%), verificar la disponibilidad del producto y emitir una alerta si el stock es bajo. Este tipo de programa es útil en sistemas de gestión de inventario, tiendas online o aplicaciones de control de almacén, donde es fundamental tener información clara y actualizada sobre los productos.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


- Primero se declara el valor del IVA como una constante `IVA = 0.21`.
- Luego se solicitan al usuario tres datos mediante input: el nombre del producto, el precio base y el stock disponible:
```
nombre_producto = input("Introducta el nombre del producto:")
precio_base = int(input("Introduce el precio del producto:"))
stock = int(input("Introduce el stock de tu producto:"))
```

- Se evalúa el stock con una estructura condicional if-elif-else para determinar si el producto está disponible o si hay pocas unidades:
```
if stock == 0:
    print("No quedan unidades")
    exit() 
elif stock <= 5:
    print("Quedan pocas unidades")
else:
    print("El producto está disponible")

```


- Después se realiza el cálculo del IVA y del precio total sumando el IVA al precio base:
```
total_iva = precio_base * IVA
precio_total = precio_base + total_iva
```

- Finalmente, se muestran todos los datos del producto en pantalla, incluyendo el nombre, precio sin IVA, stock, IVA calculado y precio total:
```
print("Producto:",nombre_producto)
print("Precio (Sin IVA):",precio_base,"€")
print("Stock:",stock)
print("IVA (21%):",total_iva,"€")
print("Precio total:",precio_total,"€")
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- A continuacion se muestra un ejercicio que, gracias a calculos y a condicionales, calcula el IVA, el precio total con IVA, la cantidad de Stock:
```
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
```

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- En este ejercicio se ha aprendido a utilizar entradas por teclado, estructuras condicionales y operaciones matemáticas básicas en Python. También se ha reforzado el uso de variables y la importancia de mostrar información clara al usuario. Este tipo de programa es muy útil en contextos reales como la gestión de productos en tiendas o almacenes, donde se necesita calcular precios con impuestos y controlar el stock. Además, se ha aplicado la lógica de programación para emitir alertas según la cantidad disponible, lo que mejora la experiencia del usuario y la eficiencia del sistema.