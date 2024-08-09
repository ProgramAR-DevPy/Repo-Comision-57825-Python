# Vistas y URLs: ¡Dirigiendo el Tráfico en tu Proyecto Django! 🚦
### Creando Vistas: ¡Las Puertas de Entrada a tu Aplicación! 🚪
- Las vistas son funciones de Python que procesan las solicitudes de los usuarios y devuelven respuestas. Son como los recepcionistas de tu aplicación, que dan la bienvenida a los visitantes y los guían hacia el contenido adecuado.

```python
#En nuestro archivo views.py de la AppCoder
from django.shortcuts import render
from .models import Curso

def inicio(req):
    return HttpResponse('vista inicio')


def cursos(req):
    return HttpResponse('vista cursos')

def profesores(req):
    return HttpResponse('vista profesores')

def estudiantes(req):
    return HttpResponse('vista estudiantes')

def entregables(req):
    return HttpResponse('vista entregables')



```

**POINT PARA PENSAR:** Que pasaría si en mi proyecto tengo que dirigir muchas aplicaciones? 🤔

```python

#LLenar en clase

```


### Organizando URLs: ¡El Mapa de tu Sitio! 🗺️
- Las URLs son las direcciones que los usuarios utilizan para acceder a diferentes partes de tu aplicación. Django utiliza un sistema de patrones de URL para mapear estas direcciones a las vistas correspondientes.


### `urls.py` en el proyecto principal:

```python
#En nuestro archivo urls.py de la AppCoder
from django.contrib import admin
from django.urls import path
from AppCoder import views


urlpatterns = [
   
    path('AppCoder/', include('AppCoder.urls')),   
  # Incluye las URLs de tu aplicación
]
```

### `urls.py` en tu aplicación (AppCoder):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('otro_ejemplo/', views.otro_ejemplo, name='otro_ejemplo'),
]
```

### HINT: Barra en URL Proyecto


### Y la onda es así:

- En el proyecto principal, include('AppCoder.urls') le dice a Django que busque patrones de URL adicionales en el archivo urls.py de tu aplicación AppCoder.
- En AppCoder/urls.py, defines los patrones de URL específicos para tu aplicación y los asocias a las vistas correspondientes.

### ¿Qué pasa si tienes muchas aplicaciones? 🤔
Si tu proyecto crece y tienes muchas aplicaciones, puedes seguir incluyendo sus URLs en el archivo principal urls.py:

```python
urlpatterns = [
    # ...
    path('AppCoder/', include('AppCoder.urls')),
    path('OtraApp/', include('OtraApp.urls')),
    # ...
]
```

#### ¡Esto mantiene tu proyecto organizado y escalable!

### Creando Plantillas (Templates): ¡El Diseño de tus Páginas! 🎨
- Las plantillas son archivos HTML que Django utiliza para generar el contenido de tus páginas web. Puedes usar variables, bucles y condicionales para hacerlas dinámicas.

### Ejemplo: AppCoder/templates/AppCoder/inicio.html

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Inicio</title>
</head>
<body>
    <h1>¡Bienvenido a mi aplicación!</h1>

    {% if cursos %}
        <h2>Lista de Cursos:</h2>
        <ul>
            {% for curso in cursos %}
                <li>{{ curso.nombre }} - Camada: {{ curso.camada }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No hay cursos disponibles.</p>
    {% endif %}
</body>
</html>
```
# Pasito a pasito, suave suavecito

1. Creamos las vistas en nuestra views.py de la Aplicacion
2. Creamos un archivo urls.py en nuestra aplicacion
3. Importamos lo necesario (`from AppCoder import views`)
4. Agregamos las vistas a las urls.py de la aplicacion (inicio, cursos, profesores, etc)
5. Ahora podemos correr el servidor así vamos viendo como va quedando.
6. Conectamos las urls de mi app con las del proyecto, para que todo haga el circuito. Vamos a `urls.py` de nuestro proyecto y en urlpatterns agregamos `path('AppCoder/', include('AppCoder.urls')`
7. Creamos una carpeta templates en nuestra app. En esta vamos a ir agregando todas las páginas (html) según las vistas que tenga en mi app. 
- me comi un paso jeje
8. Tenemos que renderizar los html.



9. Vamos con Boostrap (framework de CSS)
- HINT RUTA DE UNA WEB: 
- 1. html
- 2. css
- 3. boostrap
- 4. javascript 

10. Descargamos nuestro template: https://startbootstrap.com/
11. Creamos los archivos estaticos (son esos elementos que van a ir conformando la pagina, como ser botones, una imagen, un sidebar, un video, etc). Para tal fin, creamos una carpeta static en nuestra app. Luego dentro de esa carpeta static vamos a crear otra con el nombre que nos guste, en este caso le vamos a poner appcoder.
12. Ponemos el contenido del zip dentro de static/appcoder
13. abrimos el archivo index.html
14. Ahora cargamos los estaticos con 

```django
{% load static %}
```
15. Y ahora linkeamos
```django
<link href="{%  static 'appcoder/css/styles.css' %}" rel="stylesheet" />
<!-- Le damos la ruta: carpeta static, luego le decimos que entre a la carpeta appcoder, luego a la carpeta css, y por ultimo que lea el archivo styles.css -->
```
16. Vemos la pagina y listo el pollo!!!!