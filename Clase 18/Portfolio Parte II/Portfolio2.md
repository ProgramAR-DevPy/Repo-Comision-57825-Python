# Mejoras en las Plantillas: ¡Dale Vida a tus Páginas con Variables! ✨

- Imagina que estás escribiendo una carta ✉️. En lugar de escribir el nombre del destinatario cada vez, dejas un espacio en blanco y lo rellenas después. ¡Eso es lo que hacemos con las variables en las plantillas de Django!

- Las variables te permiten insertar información dinámica en tus plantillas, como nombres de usuarios, fechas, listas de productos, ¡lo que necesites! Esto hace que tus páginas sean más personalizadas y flexibles.

### Paso 1: Envía las Variables al Contexto 📤
En tu vista (la función de Python que renderiza la plantilla), crea un diccionario que contenga las variables que quieres pasar a la plantilla. Luego, pásale este diccionario al contexto cuando uses render.

```python
from django.shortcuts import render

def probandoTemplate(request):
    nom = "Juan"
    ap = "Perez"
    diccionario_de_contexto = {'nombre': nom, 'apellido': ap}
    
    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context(diccionario_de_contexto)  #ahora si le pasamos contexto
```

### Paso 2: Usa las Variables en tu Plantilla 🖋️
En tu plantilla HTML, utiliza la sintaxis {{ nombre_variable }} para insertar el valor de la variable en el lugar correspondiente.

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Mi Plantilla</title>
</head>
<body>
    <h1>Hola, {{ nombre }} {{ apellido }}</h1>
</body>
</html>
```

### Resultado:

Al renderizar esta plantilla, Django reemplazará {{ nombre }} y {{ apellido }} con los valores "Juan" y "Perez" respectivamente, produciendo la siguiente salida:

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Mi Plantilla</title>
</head>
<body>
    <h1>Hola, Juan Perez</h1>
</body>
</html>
```

# ¡Más Allá de las Variables Simples! 🚀

Puedes pasar todo tipo de datos al contexto, incluyendo:

- **1. Listas:** Para iterar sobre ellas en la plantilla usando bucles for.
- **2. Diccionarios:** Para acceder a sus valores usando claves.

- **3.Objetos:** Para acceder a sus atributos y métodos.
¡Las posibilidades son infinitas! Explora la documentación de Django para descubrir todas las formas en que puedes usar variables en tus plantillas.

### ¡ATENTI!

Asegúrate de que los nombres de las variables en el diccionario del contexto coincidan con los nombres que usas en la plantilla.
Si una variable no está definida en el contexto, Django mostrará un error.

# Bucles y Condicionales en Plantillas Django: ¡La Lógica Llega a tus Páginas Web! 🧠🌐
### ¿Puedo enviar datos complejos a mis plantillas? 🤔
- ¡Claro que sí! Django te permite enviar prácticamente cualquier tipo de dato a tus plantillas, incluyendo:

### Listas y tuplas: Para mostrar elementos de forma dinámica.
- Diccionarios: Para acceder a valores usando claves.
- Objetos: Para mostrar atributos y llamar a métodos.

### ¡Incluso clases personalizadas!
## Ejecutando Código Python en Plantillas: ¡La Magia de Django! ✨
Django te permite incluir lógica directamente en tus plantillas, lo que las hace más flexibles y dinámicas.

{{ }}: Para mostrar variables.
{% %}: Para bucles (for, if, etc.).
Ejemplo: Mostrar una lista de alumnos con sus notas

```python
# En tu vista (views.py)
listaDeNotas = [10, 1, 5, 3, 9]

    diccionario_de_contexto = {'nombre': nom, 'apellido': ap, "hoy": datetime.now(), "Notas": listaDeNotas}
```

```HTML
<h2>ESTE TEMPLANTE FUE CREADO EL: {{ hoy }}</h2>
    <h3> Estas son mis notas de la uni: </h3>
    <p>
        {% for n in Notas %}
        {{ n }}
        <br>
        {% endfor %}
    </p>
    <p>
        {% for n in Notas %} 
        {% if n < 4 %}
            <p style="color: red" > Nota Mala: {{ n }}</p>
        {% else %}
            <p style="color: green" > Nota Buena: {{ n }}</p>
        {% endif %}

        {% endfor %}
    </p>
```

### Cargadores de Plantillas: ¡Organiza tus Plantillas como un Profesional! 🗂️
- Cuando tienes muchas plantillas, puede ser difícil gestionarlas todas en un solo lugar. Los cargadores de plantillas te permiten organizarlas en carpetas y decirle a Django dónde encontrarlas.

### Configurando el Cargador:

Crea una carpeta para tus plantillas: (por ejemplo, templates).
En settings.py, agrega la ruta a la carpeta:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / './proyecto1/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- BASE_DIR: Es una variable especial que Django crea automáticamente. - Contiene la ruta absoluta a la carpeta raíz de tu proyecto, lo que hace que tu código sea más portable.

###  Cargando Plantillas en tus Vistas:

```python
from django.template import loader

def probando_template(request):

    nom = "Alejandro"
    ap = "Sosa"

    listaDeNotas = [10, 1, 5, 3, 9]

    diccionario_de_contexto = {'nombre': nom, 'apellido': ap, "hoy": datetime.now(), "Notas": listaDeNotas}

    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario_de_contexto)

    return HttpResponse(documento)
```


Lo que estamos haciendo:

- **Importamos loader.**
- **Obtenemos la plantilla:** `loader.get_template('template1.html') `busca la plantilla en la carpeta templates.
- **Creamos el contexto:** Un diccionario con las variables que quieres pasar a la plantilla.
- **Renderizamos la plantilla:** `plantilla.render(diccionario_de_contexto)` genera el HTML final.
- **Devolvemos una respuesta HTTP:** `HttpResponse(...)` envía el HTML al navegador.

# Modelos en Django: ¡La Base de Datos de tu Proyecto! 🏛️
- Ya conocemos las Templates (lo que se ve) y las Views (la lógica que prepara los datos para las plantillas) en Django. Ahora, ¡es hora de conocer los Modelos!

### ¿Qué es un Modelo? 🤔
- El modelo es el corazón de tu aplicación Django. Es la parte encargada de interactuar con la base de datos, permitiéndote:

- 1. **Almacenar datos:** Guardar información en la base de datos.
- 2. **Recuperar datos:** Obtener información de la base de datos.
- 3. **Modificar datos:** Actualizar la información existente en la base de datos.
- 4. **Eliminar datos:** Borrar información de la base de datos.

### Proyecto vs. Aplicación: ¡Organiza tu Código! 🗂️
- Proyecto: Es el contenedor principal de tu aplicación Django. Puede contener varias aplicaciones.
- Aplicación: Es un componente modular dentro de tu proyecto, con una funcionalidad específica. Cada aplicación tiene sus propios modelos, vistas, plantillas, etc.

**Es buena práctica dividir tu proyecto en varias aplicaciones para mantener el código organizado y facilitar su mantenimiento.**

### Creando una Aplicación: ¡Manos a la Obra! 🛠️

- 1. **Crea un nuevo proyecto:** `django-admin startproject ProyectoCoder`
- 2. **Entra en la carpeta del proyecto:** `cd ProyectoCoder`
- 3. **Crea una aplicación:** `python manage.py startapp AppCoder`

### Definiendo Modelos: ¡El Plano de tu Base de Datos! 📐

- Dentro de tu aplicación, crea un archivo llamado models.py. Aquí definirás tus modelos, que representan las tablas de tu base de datos.

### Ejemplo: Modelos para una aplicación de cursos

```python
from django.db import models

#AHORA CREAMOS TABLAS

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)   

    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()   
```

### ¡Informa a Django sobre tu Aplicación! 📣
- Abre el archivo settings.py en tu proyecto.
Busca la lista INSTALLED_APPS y agrega el nombre de tu aplicación:

```python
INSTALLED_APPS = [
    # ... otras aplicaciones ...
    'AppCoder',  # Agrega tu aplicación aquí
]
```
### Creando la Base de Datos: ¡La Magia de Django! ✨
- Django se encarga de crear y gestionar tu base de datos. Solo tienes que ejecutar estos comandos:

1. Generar las migraciones: python manage.py makemigrations
2. Aplicar las migraciones: python manage.py migrate

- #### ¡Listo! Django ha creado las tablas en tu base de datos según tus modelos.

#### Creando Tablas en tu Base de Datos con Modelos de Django 🗄️
El siguiente cofigo crea cuatro modelos en Django: Curso, Estudiante, Profesor y Entregable. Cada uno de estos modelos representa una tabla en tu base de datos, y los atributos dentro de cada modelo definen las columnas de esas tablas.

- Veamos cada modelo en detalle:

- 1. Curso

```python
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
```

- nombre: Una columna de tipo CharField (cadena de caracteres) que puede almacenar hasta 40 caracteres. Esto se usará para guardar el nombre del curso, por ejemplo, "Python", "Matemáticas", etc.
- camada: Una columna de tipo IntegerField (número entero) que se usará para almacenar el número de la camada o cohorte del curso.

- 2. Estudiante
```python
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
```


- nombre: Almacena el nombre del estudiante (hasta 30 caracteres).
- apellido: Almacena el apellido del estudiante (hasta 30 caracteres).
- email: Una columna especial para almacenar direcciones de correo electrónico. Django se encargará de validar que el valor ingresado tenga un formato de email válido.

3. Profesor

```python
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
```

- nombre, apellido, email: Similares a los de la clase Estudiante.
- profesion: Almacena la profesión del profesor (hasta 30 caracteres).

- 4. Entregable
```python
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField() 
```

- nombre: Almacena el nombre del entregable (hasta 30 caracteres).
- fecha_de_entrega: Una columna de tipo DateField para almacenar la fecha en que se debe entregar el trabajo.
- entregado: Una columna de tipo BooleanField (booleano) que indica si el entregable ha sido entregado o no (True o False).






### Explorando tu Base de Datos: ¡Usa DB Browser! 🔎
Puedes usar una herramienta como DB Browser for SQLite para ver y editar tu base de datos de forma visual.

### Agregando Datos: ¡Dale Vida a tu Base de Datos! 🌱
Puedes agregar datos a tu base de datos desde la consola de Django o directamente desde DB Browser.

### Ejemplo en la consola:

```python
from AppCoder.models import Curso

curso = Curso(nombre="Python", camada=23800)
curso.save()
```
