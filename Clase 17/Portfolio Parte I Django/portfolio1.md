# Entornos Virtuales y Paquetes en Python: ¡Organización y Portabilidad! 📦
### Entornos Virtuales: Tu Caja de Herramientas Personalizada 🧰
- Imagina que eres un carpintero. Tienes muchas herramientas, pero no las necesitas todas para cada proyecto. Los entornos virtuales en Python son como cajas de herramientas separadas para cada proyecto. Puedes tener una caja para construir una mesa, otra para una silla, y así sucesivamente.

### ¿Por qué usar entornos virtuales? 🛠️
- **Evitar conflictos:** Cada proyecto puede tener sus propias versiones de bibliotecas (paquetes) sin interferir entre sí.
- **Organización:** Mantiene las dependencias de cada proyecto aisladas y ordenadas.
- **Portabilidad:** Facilita compartir tu proyecto con otros, ya que incluye todas las bibliotecas necesarias en el entorno virtual.

### Creando un Entorno Virtual con venv 🐍
- 1. **Instalar virtualenv:** 
```bash
pip install virtualenv
```

- 2. **Crear el entorno:**

```bash
python -m venv nombre_de_tu_entorno
```

Esto creará una carpeta con el nombre que le diste, que contendrá:

- Una copia del intérprete de Python.
- Un directorio lib para instalar las bibliotecas del proyecto.
- Otros archivos de configuración.

### Activar el entorno:

- **Windows:** nombre_de_tu_entorno\Scripts\activate
- **macOS/Linux:** source nombre_de_tu_entorno/bin/activate
Verás que el nombre del entorno aparece entre paréntesis al principio de tu línea de comandos, indicando que está activo.

- **Instalar paquetes:** Usa pip install para instalar las bibliotecas necesarias para tu proyecto. Estas se instalarán dentro del entorno virtual, no a nivel global.

- **Desactivar el entorno:** Escribe deactivate cuando hayas terminado de trabajar en el proyecto.


¡Organización y Colaboración! 🤝
Los entornos virtuales y los paquetes son herramientas esenciales para mantener tus proyectos Python organizados, evitar conflictos entre dependencias y facilitar la colaboración con otros desarrolladores. ¡Úsalos en tus proyectos y verás la diferencia!



**Siempre activa el entorno virtual correspondiente antes de trabajar en un proyecto.**

### A tener en cuenta:
- Utiliza `pip freeze > requirements.txt` para generar un archivo con las dependencias de tu proyecto, facilitando su instalación en otros entornos.



# Django: El Framework Web de Python para Construir Aplicaciones Robustas 🚀
#### ¿Qué es Django? 💡
- **Imagina que quieres construir una casa. Podrías hacerlo ladrillo por ladrillo, pero eso llevaría mucho tiempo y esfuerzo. Django es como un kit de construcción pre-fabricado que te proporciona las herramientas y la estructura necesarias para construir tu aplicación web de manera más rápida y eficiente.**

#### HINT VERSION DE DJANGO

### ¿Por qué usar Django? 🏗️
- 1. **Baterías incluidas:** Django viene con muchas funcionalidades integradas (autenticación de usuarios, administración de bases de datos, formularios, etc.), lo que te ahorra tiempo y esfuerzo.
- 2. **Estructura clara:** Django sigue el patrón de diseño MTV (Modelo-Template-Vista), que separa la lógica de la aplicación, la presentación y la interacción con el usuario, haciendo que tu código sea más organizado y fácil de mantener.
- 3. **Escalable:** Django está diseñado para manejar proyectos de cualquier tamaño, desde pequeños sitios web personales hasta grandes aplicaciones empresariales.
- 4. **Comunidad activa:** Django tiene una gran comunidad de desarrolladores que contribuyen con documentación, tutoriales y plugins.

### Fundamentos de Django: MTV 🖼️
- **Model(Modelo):** Define la estructura de tus datos y cómo se almacenan en la base de datos.
- **Template (Plantilla):** Controla la presentación de los datos al usuario (HTML, CSS, etc.).
- **View (Vista):** Maneja la lógica de la aplicación y la interacción entre los modelos y las plantillas.

### Creando tu Primer Proyecto Django 🎬
- **Instalar Django:** 
```bash
pip install django
```
- **Crear el proyecto:**
```bash 
django-admin startproject mi_proyecto
```

- **Crear vistas:** Escribe funciones en views.py para manejar las solicitudes de los usuarios.
- **Definir URLs:** Configura las rutas en urls.py para conectar las vistas con las URLs.
- **Crear plantillas:** Diseña las plantillas HTML en la carpeta templates (o el nombre que le pongas a la carpeta).
- **Ejecutar migraciones:** 

```bash
python manage.py migrate #para crear las tablas en la base de datos.
```
- **Iniciar el servidor de desarrollo:** 
python manage.py runserver



### ¡Tu Proyecto! 🎉
- Una vez que hayas completado estos pasos, podrás acceder a tu aplicación Django en tu navegador web. ¡Felicidades por dar tus primeros pasos en el mundo de Django!

No te olvides:

Django es un framework poderoso con muchas funcionalidades. ¡Mirá la documentación oficial para aprender más! https://docs.djangoproject.com/es/5.0/

### La práctica es clave para dominar Django.

# Nuestro Primer View y Plantillas en Django: ¡La Magia de la Separación! ✨
### Creando Nuestra Primera Vista (View) 🎬
- **Archivo views.py:** Crea un archivo llamado views.py en la misma carpeta donde tienes urls.py, settings.py, etc.

### Importar HttpResponse:

```python
from django.http import HttpResponse
```

### Definir la vista saludo:

```python
def saludo(request):
    return HttpResponse("Hola Django - Coder")
```

### Configurar la URL en urls.py:

```python
from django.urls import path
from Proyecto1.views import saludo  # Importa las vistas de tu aplicación

urlpatterns = [
    path('saludo/', saludo),  # Conecta la URL /saludo/ a la vista saludo
]
```

### Ejecutar el servidor:

```bash
python manage.py runserver
```

- Acceder a la vista: Abre tu navegador y visita http://127.0.0.1:8000/saludo/. ¡Verás tu primer saludo desde Django!

### Agregando Otra Vista y Usando HTML 🖼️

Puedes crear más vistas de la misma manera. Incluso puedes incluir código HTML directamente en la respuesta HttpResponse:

```python
def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")
```

### Pasaje de Parámetros: Dinamismo en tus Vistas 🔄
- Puedes hacer que tus vistas sean más dinámicas pasando parámetros desde Python:

```python
from datetime import date

def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")
```

### Parámetros desde la URL: ¡Personalización! 🎯
- Django te permite capturar información de la URL y usarla en tus vistas:

```python
def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")
```

### Configura la URL en urls.py:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('muestra_nombre/<nombre>/', muestra_nombre),
]
```

- **Ahora puedes acceder a http://127.0.0.1:8000/saludar/Maria/ y la vista mostrará "¡Hola, Maria!".**
#### HINT PAGINA DE DJANGO SEARCH

### Plantillas Django: ¡Separando la Lógica de la Presentación! 🎨
- Las plantillas te permiten crear archivos HTML separados que Django puede llenar con datos dinámicos desde tus vistas.

- **Crea una carpeta plantillas:** Dentro de tu proyecto, crea una carpeta llamada plantillas.

- **Crea un archivo HTML:** Dentro de templates, crea un archivo template1.html.

- **Escribe tu HTML:** Agrega el contenido HTML que deseas mostrar.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hola, esta es nuestra primer plantilla!
</body>
</html>
```

### Usa la plantilla en tu vista:

```python
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('./Clases_Coder/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
```


## ¡El Poder de MTV! 💪
Con el patrón MTV de Django, puedes:

- **Separar la lógica de la presentación:** Los diseñadores trabajan en las plantillas HTML, mientras que los desarrolladores se enfocan en la lógica de Python en las vistas.
- **Reutilizar plantillas:** Puedes crear plantillas base y extenderlas en otras plantillas para evitar repetir código.
- **Crear aplicaciones web más mantenibles y escalables:** La separación de responsabilidades facilita la modificación y el crecimiento de tu proyecto.