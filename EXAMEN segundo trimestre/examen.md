- Mi proyecto es una pagina web de alquiler de rings de boxeo, he querido hacer una web seria y sin mucha tonteria, pero funcional. En este caso, voy a enfocarme en el tema de programacion, algo esencial, gracias a esto podemos unir el HTML con la base de datos. La web permite al usuario elegir entre dos rings de boxeo (profesional o entrenamiento), cuando el usuario escoja el ring deseado, se le pedira que inicie sesion o que se registre en caso de que no tenga cuenta. Una vez el usuario haya entrado con su cuenta, se le va a facilitar un calendario para que seleccione el dia que quiere hacer la reserva, una vez elegido el dia, apareceran unas casillas con las horas que esten disponibles, cuando el usuario elija la hora que desea y confirme la reserva, esta reserva sera guardada en `mis reservas`, donde el usuario podra entrar siempre que quiera iniciando sesion. A continuacion, muestro la estructura de carpetas de mi proyecto:
```
├── app.py
├── basededatos
│   └── base.sql
├── static
│   ├── estilo.css
│   ├── logo_ig.png
│   ├── logo_maps.png
│   ├── ring1.jpg
│   └── ring2.jpg
└── templates
    ├── index.html
    ├── login.html
    ├── mis_reservas.html
    ├── registro.html
    └── reservar.html
```


- Este archivo `app.py` es el corazon de la web, aquí es donde Flask controla todas las rutas, se conecta a la base de datos y decide qué HTML tiene que mostrarse en cada momento. Cada vez que el usuario visita una pagina, hace clic en un boton o envia un formulario, Flask recibe esa peticion, consulta la base de datos si hace falta, y devuelve una plantilla HTML con los datos actualizados usando Jinja.

**LIBRERIAS**

- Para empezar, importamos las librerias que vamos a utilizar en nuestra web, en este caso son las siguientes:

    - `Flask` para crear la app, renderizar, recoger datos...
    - `Mysql.connector` para abrir conexion con MySQL
    - `Werkzeug.securiti` para encriptar las contraseñas

```
from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

```


- Instanciamos Flask con el comando `app = Flask(__name__)`



**CONEXION A LA BASE DE DATOS**

- Para conectarnos a la base de datos tenenemos que crear la siguiente funcion:
```
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="daniel",
        password="Dani12345&",
        database="rings_boxeo"
    )
```

- Esta funcion abre una conexion a la base de datos, en la que hemos tenido que crear previamente ese usuario y esa contraseña




**PAGINA DE INICIO**


- Para la pagina de inicio he creado este funcion para consultar los rings. Esta funcion coge la informacion de los rings gracias a `cursor.execute("SELECT * FROM rings")` , despues, `index.html` recibe la informacion de los rings gracias a `return render_template("index.html", rings=rings)` y los recorre con `{% for ring in rings %}` para pintar tarjetas.
```
@app.route("/")
def index():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rings")
    rings = cursor.fetchall()
    conexion.close()
    return render_template("index.html", rings=rings)
```





**REGISTRO**


- Para el apartado de registro, primero creamos esta funcion, que unicamente muestra el formulario de registro:
```
@app.route("/registro")
def registro():
    return render_template("registro.html")
```


- Despues, creamos otra funcion para guardar el usuario, esta funcion hace que recibamos los datos de registro:
```
@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s,%s,%s)", (nombre, email, password))
        conexion.commit()
    except:
        return "El email ya está registrado."
    finally:
        conexion.close()
    return redirect(url_for("login"))
```

- En la primera parte del codigo:
```
nombre = request.form["nombre"]
email = request.form["email"]
password = generate_password_hash(request.form["password"])
```

    - Recibimos lo que el usuario pone en el formulario
    - La contraseña es encriptada gracias a `generate_password_hash(request.form["password"])`


- Despues, insertamos estos datos en la base de datos usando `cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s,%s,%s)", (nombre, email, password))`

- En caso de que el email ya exista, se devuelve `return "El email ya está registrado."`


- Si todo va bien, redirigimos al usuario al login, usando `return redirect(url_for("login"))`





**LOGIN**

- Para el apartado de login, primero creamos esta funcion, que unicamente muestra el formulario de registro:
```

@app.route("/login")
def login():
    return render_template("login.html")
```


- Despues, creamos otra funcion para recibir los datos de login:
```
@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    email = request.form["email"]
    password = request.form["password"]
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
    usuario = cursor.fetchone()
    conexion.close()

    if usuario and check_password_hash(usuario["password"], password):
        session["usuario_id"] = usuario["id"]
        session["usuario_nombre"] = usuario["nombre"]
        return redirect("/")
    return "Login incorrecto. <a href='/login'>Reintentar</a>"
```

- En la primera parte del codigo recibimos lo que el usuario escribe en el formulario:
```
@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    email = request.form["email"]
    password = request.form["password"]
```

- Despues, bucamos el email en la base de datos:
```
cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
usuario = cursor.fetchone()
```

- Despues, comparamos la contraseña:
```
if usuario and check_password_hash(usuario["password"], password):
```

- Si todo es correcto:
```
session["usuario_id"] = usuario["id"]
session["usuario_nombre"] = usuario["nombre"]
return redirect("/")

```

- Si hay algun fallo se muestra el siguiente mensaje:
```
return "Login incorrecto. <a href='/login'>Reintentar</a>"
```




**LOGOUT**

- Esta funcion cierra la sesion del usuario:
```
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

```




**RESERVAR UN RING**


- Primero creamos la funcion `reservar`:
```
@app.route("/reservar/<int:id_ring>")
def reservar(id_ring):
    if "usuario_id" not in session: return redirect("/login")
    
    fecha = request.args.get('fecha')
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rings WHERE id=%s", (id_ring,))
    ring = cursor.fetchone()
    
    horas_ocupadas = []
    if fecha:
        cursor.execute("SELECT hora FROM reservas WHERE id_ring=%s AND fecha=%s", (id_ring, fecha))
        horas_ocupadas = [r['hora'] for r in cursor.fetchall()]
    
    conexion.close()
    return render_template("reservar.html", ring=ring, fecha=fecha, horario=range(9, 21), ocupadas=horas_ocupadas)
```

- Primero comprobamos si el usuario esta logueado usando:
```
if "usuario_id" not in session: 
    return redirect("/login")

```

- En caso de que no este logueado, lo manda al login




- Obtenemos la fecha seleccionada:
```
fecha = request.args.get('fecha')
```

- Cargamos los datos del ring seleccionado:
```
cursor.execute("SELECT * FROM rings WHERE id=%s", (id_ring,))
ring = cursor.fetchone()

```


- Calculamos que horas estan ocupadas:
```
cursor.execute("SELECT hora FROM reservas WHERE id_ring=%s AND fecha=%s", (id_ring, fecha))
horas_ocupadas = [r['hora'] for r in cursor.fetchall()]

```


- Todo esto es enviado a `reservar.html` gracias a:
```
return render_template("reservar.html",
    ring=ring,
    fecha=fecha,
    horario=range(9, 21),
    ocupadas=horas_ocupadas
)

```




**GUARDAR RESERVA**

- Creamos la funcion `guardar_reserva`:
```
@app.route("/guardar_reserva", methods=["POST"])
def guardar_reserva():
    if "usuario_id" not in session: return redirect("/login")
    
    id_usuario = session["usuario_id"]
    id_ring = request.form["id_ring"]
    fecha = request.form["fecha"]
    hora = request.form["hora"]

    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO reservas (id_usuario, id_ring, fecha, hora) VALUES (%s,%s,%s,%s)", (id_usuario, id_ring, fecha, hora))
        conexion.commit()
        return redirect("/mis_reservas")
    except:
        return "Error: Hora ya reservada."
    finally:
        conexion.close()
```


- Volvemos a comprobar si el usuario esta logueado:
```
if "usuario_id" not in session: return redirect("/login")
```

- Luego recogemos lo que el usuario ha elegido:
```
id_usuario = session["usuario_id"]
id_ring = request.form["id_ring"]
fecha = request.form["fecha"]
hora = request.form["hora"]
```


- Guardamos la reserva:
```
cursor.execute(
    "INSERT INTO reservas (id_usuario, id_ring, fecha, hora) VALUES (%s,%s,%s,%s)",
    (id_usuario, id_ring, fecha, hora)
)
```

- Si la hora esta ocupada, da error; si no lo esta, redirige a `mis reservas`




**MIS RESERVAS**

- Creamos la funcion `mis_reservas`:
```
@app.route("/mis_reservas")
def mis_reservas():
    if "usuario_id" not in session: return redirect("/login")
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.fecha, r.hora, rings.nombre, rings.precio 
        FROM reservas r JOIN rings ON r.id_ring = rings.id 
        WHERE r.id_usuario = %s ORDER BY r.fecha DESC
    """, (session["usuario_id"],))
    reservas = cursor.fetchall()
    conexion.close()
    return render_template("mis_reservas.html", reservas=reservas)

if __name__ == "__main__":
    app.run(debug=True)
```

- Consultamos todas las reservas del usuario:
```
SELECT r.fecha, r.hora, rings.nombre, rings.precio 
FROM reservas r 
JOIN rings ON r.id_ring = rings.id 
WHERE r.id_usuario = %s 
ORDER BY r.fecha DESC
```


- Eviamos el resultado al archivo html:
```
return render_template("mis_reservas.html", reservas=reservas)
```



- En general, este proyecto me ha servido para entender cómo encajan todas las piezas de una aplicación web real: el HTML y el CSS para construir y dar estilo a las páginas, Flask para controlar las rutas y la lógica, y MySQL para guardar la información de usuarios, rings y reservas. He intentado crear una web sencilla, directa y sin excesos, pero que funcione bien y que el usuario pueda usar sin líos.
También he aprendido la importancia de cosas como cifrar contraseñas, gestionar la sesión del usuario o evitar que dos personas reserven la misma hora.
Aunque todavía hay cosas que se podrían mejorar, como añadir un panel de administración o ampliar las opciones de usuario, el resultado cumple con lo que buscaba: una web funcional, ordenada y útil. Y sobre todo, un proyecto donde he podido aplicar todo lo que he aprendido de lenguajes de marcas, backend y bases de datos de una forma práctica y completa.