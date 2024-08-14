# Herencia de Templates en Django: ¡Reutiliza y Organiza tu Diseño! ♻️
- Imagina que tienes una plantilla de currículum vitae 📄. En lugar de copiar y pegar la misma información básica (nombre, contacto, educación) en cada versión, creas una plantilla maestra y luego personalizas solo las secciones relevantes para cada trabajo. ¡Eso es herencia de plantillas en Django!

- La herencia de plantillas te permite crear una plantilla "base" con elementos comunes (encabezado, pie de página, menú de navegación) y luego crear plantillas "hijas" que heredan esa estructura y solo definen el contenido específico de cada página.

### ¿Por qué usar herencia de plantillas? 🤔
- **Reutilización de código:** Evita la repetición de código HTML en múltiples plantillas.
- **Consistencia**: Mantiene un diseño uniforme en todo tu sitio web.
- **Mantenimiento más fácil**: Si necesitas cambiar algo en la plantilla base, el cambio se reflejará automáticamente en todas las plantillas hijas.

### Creando una Plantilla Base: ¡El Cimiento de tu Diseño! 🧱

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Título por defecto{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Mi Sitio Web</h1>
        <nav>
            </nav>
    </header>

    <main>
        {% block contenidoQueCambia %}{% endblock %} 
    </main>

    <footer>
        <p>&copy; 2023 Mi Empresa</p>
    </footer>
</body>
</html>
```

- ` {% block ... %}:` Define bloques de contenido que las plantillas hijas pueden reemplazar o extender.
- `{% endblock %}:` Marca el final de un bloque.
contenidoQueCambia: Es el nombre del bloque que contendrá el contenido específico de cada página hija.

### Creando Plantillas Hijas: ¡Personaliza tu Contenido! 🎨
```HTML
{% extends "AppCoder/padre.html" %}  {% load static %}

{% block title %}Página de Inicio{% endblock %}

{% block contenidoQueCambia %}
    <h1>Este es el título del Inicio</h1>
    <p>Se ha heredado todo desde la plantilla padre</p>
    <h3>En el hijo, inicio.html, casi no hay nada :)</h3>
{% endblock %}
```

- `{% extends "AppCoder/padre.html" %}:` Indica que esta plantilla hereda de padre.html.
- `{% block ... %}:` Redefine los bloques de contenido definidos en la plantilla padre.

### ¡Resultado Final! 🎉
Al renderizar inicio.html, Django combinará el contenido de la plantilla hija con la estructura de la plantilla padre, produciendo una página completa con el encabezado, pie de página y menú de navegación de la plantilla base, y el contenido específico de la página de inicio.

### **¡Importante!**

Asegúrate de que tus plantillas estén ubicadas en la carpeta correcta (templates en la raíz de tu proyecto o dentro de la carpeta templates de tu aplicación).
Si no ves los cambios reflejados en tu navegador, asegúrate de reiniciar el servidor de desarrollo de Django.


# Paso a Paso Herencia de Templates

1. **Creamos un archivo padre.html en nuestra app. Y le pegamos todo el contenido del archivo inicio.html o index.html (siempre en la app)**

2. **Dentro de padre.html ponemos el siguiente bloque <br>`{% block contenidoQueCambia %}` <br> Ahora todo lo que este por fuera es fijo. Es decir se muestra para todos lo mismo, menos lo que pongamos aca adentro. <br> `{% endblock %}`.**

3. Ahora vamos a un html hijo, es decir cualquiera que no sea padre. En este ejemplo vamos a ir a cursos.html y ponemos el siguiente bloque <br> 

```html
<!-- En cursos.html -->
{% extends "AppCoder/padre.html" %}

{% load static %}

{% block contenidoQueCambia %} 

<!--Aquí va lo que cambia, y lo asociado a está vista :) -->
    <h1>Este es el título del Inicio que cambio</h1>
    <p>Se ha heredado todo desde la plantilla padre</p>
    <h3>En el hijo, inicio.html, casí no hay nada :)</h3>

{% endblock %}
```
4. Ejecutamos nuestro servidor `python manage.py runserver`



# Navegar entre nuestros templates

1. En nuesto padre.html buscamos el la etiqueda 
```html  

<nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
            <div class="container px-5">
                <a class="navbar-brand" href="#page-top">CodificAr Dev Demo</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="{% url 'inicio'%}">Inicio</a></li>  //Le indicamos a donde va cuando toco el boton inicio. Le indico por medio de la url y el nombre correspondiente.
                        <li class="nav-item"><a class="nav-link" href="{% url 'cursos' %}">Cursos</a></li>
                        <li class="nav-item"><a class="nav-link" href="{%  url 'profesores' %}">Profesores</a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'estudiantes' %}">Estudiantes</a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'entregables'%}">Entregables</a></li>
                        <li class="nav-item"><a class="nav-link" href="{#!}">Iniciar Sesión</a></li>
                        <li class="nav-item"><a class="nav-link" href="#!">Registrarse</a></li>
                    </ul>
                </div>
            </div>
        </nav>

```
2. AHora vamos a cursos.html y le damos todo el contenido que queremos que tenga cursos. En este ejemplo le doy las secciones que antes estaban en nuestro archivo inicio.html o index.html

```html
{% extends "appcoder/padre.html" %}
    {% load static %}
    {% block contenidoQueCambia %}
   <!-- Content section 1-->
    <section id="scroll">
        <div class="container px-5">
            <div class="row gx-5 align-items-center">
                <div class="col-lg-6 order-lg-2">
                    <div class="p-5"><img class="img-fluid rounded-circle" src="{% static 'appcoder/assets/img/01.jpg' %}" alt="..." /></div>
                </div>
                <div class="col-lg-6 order-lg-1">
                    <div class="p-5">
                        <h2 class="display-4">For those about to rock...</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod aliquid, mollitia odio veniam sit iste esse assumenda amet aperiam exercitationem, ea animi blanditiis recusandae! Ratione voluptatum molestiae adipisci, beatae obcaecati.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Content section 2-->
    <section>
        <div class="container px-5">
            <div class="row gx-5 align-items-center">
                <div class="col-lg-6">
                    <div class="p-5"><img class="img-fluid rounded-circle" src="{% static 'appcoder/assets/img/02.jpg' %}" alt="..." /></div>
                </div>
                <div class="col-lg-6">
                    <div class="p-5">
                        <h2 class="display-4">We salute you!</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod aliquid, mollitia odio veniam sit iste esse assumenda amet aperiam exercitationem, ea animi blanditiis recusandae! Ratione voluptatum molestiae adipisci, beatae obcaecati.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Content section 3-->
    <section>
        <div class="container px-5">
            <div class="row gx-5 align-items-center">
                <div class="col-lg-6 order-lg-2">
                    <div class="p-5"><img class="img-fluid rounded-circle" src="{% static 'appcoder/assets/img/03.jpg' %}" alt="..." /></div>
                </div>
                <div class="col-lg-6 order-lg-1">
                    <div class="p-5">
                        <h2 class="display-4">Let there be rock!</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quod aliquid, mollitia odio veniam sit iste esse assumenda amet aperiam exercitationem, ea animi blanditiis recusandae! Ratione voluptatum molestiae adipisci, beatae obcaecati.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    {% endblock %}

```
3. Ahora vamos a nuestro modulo `urls.py` en nuestra app. Y le indicamos lo siguiente

```python

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),  #Le damos un nuevo argumento, indicando el nombre de la vista. para que al tocar cada boton, django sepa a donde ir.
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    
]
```

###  SE VA PONIENDO LINDA LA COSA. AHORA VAMOS POR EL ADMIN PANEL DE DJANGO

Pero primero vamos a ver algo que quedo pendiente de otra clase. Se acuerdan que aprendimos como agregar datos a nuestra BD (base de datos) desde una url (que no es una buena practica) pero lo hicimos por que estamos aprendiendo. Ahora vamos a ver como podemos agregar datos desde la consola para ejecutar una shell interactiva de python en django.

1. Ejecutamos en la terminal `python manage.py shell`

2. Se va a abrir una shell interactiva de python. La cual nos va a permitir interactuar con nuestra base de datos. Primero importamos:

```python
from AppCoder.models import Curso #y tocamos enter.
```
3. Creamos una instancia, es decir creamos un curso.

```python
curso = Curso(nombre= "Go", camada= "1999")  #Enter
```
4. Guardamos el curso en nuestra bd

```python
curso.save() #Enter
```
5. Verificamos en nuestra `BD` el nuevo curso.

6. Ejecutamos exit() para salir de la shell.


#### CONTINUAMOS CON NUESTRO ADMIN PANEL

1. Primero tenemos que importar los modelos que queremos administrar, es decir, los modelos que estan en la `BD`. Para eso vamos a nuestro modulo admin.py (si no existe lo creamos) e importamos nuestos modelos (siempre en nuestra app).

```python
from django.contrib import admin
from AppCoder.models import Curso, Estudiante, Profesor, Entregable


# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)

```
2. Ahora tenemos que crear un usuario, ya que si entramos a 
http://127.0.0.1:8000/admin/ nos va a pedir un usuario y una contraseña. Por lo que en nuestra consola ejecutamos:

`python manage.py createsuperuser` y ponemos los datos que nos solicita. Y tienen que tener en cuenta que al teclear la contraseña hay que hacerlo bien, ya que por pantalla no se ve nada de lo que tecleamos. Y así debe ser. Por lo que pongan bien sus dedos xD

3. Ahora si, vamos a http://127.0.0.1:8000/admin/ e ingresamos con nuestros datos recien generados. Si es necesario, volver a ejecutar nuestro servidor. 

4. El super usuario es el que va a poder administar todo en nuestro panel. Por lo que es recomendable que si hay un equipo de trabajo, agreguemos nuevos usuarios pero sin tantos privilegios como el superusuario. Por lo que vamos a ver en vivo como agregamos un nuevo usuario y sus permisos. 

5. Seguimos en vivo y vamos a crear una nueva instancia desde nuestro admin panel. 







