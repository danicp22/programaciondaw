A continuacion se desarrolla el ejercicio propuesto con Notas musicales y Octavas, creando un programa que muestre
la nota y la octava.

Para esto se utiliza principalmente en nuestro programa el bucle for, mas especificamente un doble bucle, que es
una estructura de control que en nuestro ejercicio ,nos permite creando una varible para asignar un limite que
serian la cantidad de notas y octavas, asi:

for(var nota= 1; nota <7;nota++){
   for(var octava= 1; octava <=5;octava++)
}
Y luego ejecutar con un "document.write" la lista completa que nos muestra
la nota y la octava:
{
    document.write("Nota ", nota," de la octava ", octava,"<br>")
   }

'''
<script>
    /*PROGRAMA NOTAS MUSICALES
    v.01 Andres Julian Ramirez
    Este programa muestra combinaciones posibles de octavas y notas*/


for(var nota= 1; nota <7;nota++){
   for(var octava= 1; octava <=5;octava++){
    document.write("Nota ", nota," de la octava ", octava,"<br>")
   }
}


</script>

'''

Podemos concluir que un bucle for nos permite automatizar y acortar tareas que nos pueden tomar mas tiempo, como crear una lista
de todas las combinaciones las notas y octavas de un piano y asi por ejemplo usando un condicional distinguir o categorizar informacion.


