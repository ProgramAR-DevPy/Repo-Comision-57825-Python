# Formularios en Django: ¡La Puerta de Entrada para tus Datos! 🚪
- Los formularios son elementos esenciales en cualquier aplicación web. Permiten a los usuarios interactuar con tu sitio, proporcionando información que luego puedes procesar y almacenar en tu base de datos.

### ¿Cómo funcionan los formularios en Django? 🤔
- **HTML:** Creas un formulario en tu plantilla HTML utilizando etiquetas `<form>`, `<input>`, `<button>`, etc.
- **Vista:** Defines una vista en Django que maneja las solicitudes del formulario.
- **URL:** Configuras una URL en tu archivo urls.py para que Django sepa a qué vista enviar la información del formulario.

### Método GET o POST: El formulario envía los datos al servidor usando uno de estos métodos:

1. **GET:** Se usa para solicitudes simples, como búsquedas, donde los datos se envían en la URL.
2. **POST:** Se usa para enviar datos más sensibles o grandes, como información de registro o formularios de contacto. Los datos se envían en el cuerpo de la solicitud HTTP.

#### Creando un Formulario HTML Básico:

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   

    <title>Formulario - Agregar Curso</title>
</head>
<body>
    <form action="/cursoFormulario/" method="post"> 
        <p> Curso: <input type="text" name="curso"> </p>
        <p> Camada: <input   
 type="text" name="camada"> </p>
        <input type="submit" value="Enviar">
    </form>   
 
</body>
</html>
```

### Y el temita funciona así:

```HTML
<form action="/cursoFormulario/" method="post">:
```
- **action:** Indica la URL a la que se enviarán los datos del formulario cuando el usuario haga clic en el botón "Enviar".
- **method:** Especifica el método HTTP que se utilizará para enviar los datos (en este caso, "post").
```HTML
<input type="text" name="curso"> y <input type="text" name="camada">:
```
- **type="text":** Crea campos de texto donde el usuario puede ingresar información.
- **name:** Asigna un nombre a cada campo. Estos nombres se usarán para identificar los datos enviados al servidor.

```HTML
<input type="submit" value="Enviar">:
```

- **type="submit":** Crea un botón que, al hacer clic, envía los datos del formulario al servidor.
value="Enviar": El texto que se mostrará en el botón.

### Próximos pasos:
Crear una vista en views.py para manejar la solicitud del formulario y procesar los datos.
Agregar una URL en urls.py para mapear la URL del formulario a la vista correspondiente.
¡Con estos pasos básicos, podrás crear formularios en Django y empezar a recopilar información de tus usuarios!



# Creación de Formularios con Django Forms: ¡Más Sencillo y Potente! 💪
- Django Forms nos permite crear y manejar formularios de manera más estructurada y eficiente, separando la lógica del formulario de la presentación HTML. ¡Es como tener un asistente que se encarga de la parte aburrida y te deja enfocarte en el diseño! 🤖

### 1. Creando el Formulario en forms.py
```python
from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
```

- `from django import forms:` Importamos el módulo forms de Django, que contiene las clases y herramientas necesarias para crear formularios.
- `class CursoFormulario(forms.Form):` Definimos una clase llamada CursoFormulario que hereda de forms.Form. Esta clase representa nuestro formulario.
- `curso = forms.CharField():` Creamos un campo de formulario llamado curso de tipo CharField (cadena de caracteres). Esto representará un campo de texto en el formulario HTML.
`camada = forms.IntegerField():` Creamos otro campo llamado camada de tipo IntegerField (número entero). Esto representará un campo numérico en el formulario.
### 2. Usando el Formulario en la Vista
```python
from django.shortcuts import render
from AppCoder.forms import CursoFormulario

def cursoFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = CursoFormulario(request.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])  # Creamos un objeto Curso
            curso.save()  # Guardamos el curso en la base de datos
            return render(request, "AppCoder/inicio.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = CursoFormulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})
```

### Esto funciona así:

- **Importamos el formulario:** `from AppCoder.forms import CursoFormulario`
- **Manejo de la solicitud POST:**
- `if request.method == "POST":` Verifica si el formulario fue enviado usando el método POST.
- `miFormulario = CursoFormulario(request.POST):` Crea un objeto formulario y lo llena con los datos enviados en la solicitud POST.
- `if miFormulario.is_valid():` Valida los datos del formulario. 
#### Si son válidos:
- `informacion = miFormulario.cleaned_data:` Obtiene los datos limpios y validados del formulario.
- Crea un objeto Curso con los datos del formulario.
- Guarda el objeto Curso en la base de datos.
- Redirige a la página de inicio.

#### Manejo de la solicitud GET (o inicial):
- `miFormulario = CursoFormulario():` Crea un formulario vacío para mostrarlo al usuario.
- Renderizado de la plantilla:
Pasa el objeto miFormulario al contexto de la plantilla cursoFormulario.html.

### 3. Mostrando el Formulario en la Plantilla
```HTML
<form method="post">
    {% csrf_token %}  {# Protección CSRF de Django #}
    {{ miFormulario.as_table }}<!-- Renderiza los campos del formulario  -->
    <button type="submit">Enviar</button>
</form>
```

- `{% csrf_token %}:` Es esencial para proteger tu formulario contra ataques CSRF.
- `{{ miFormulario.as_p }}:` Renderiza los campos del formulario como párrafos (`<p>`). Puedes usar otros métodos como as_table o as_ul para diferentes estilos de presentación.

### Ventajas de usar Django Forms:

- **Validación automática:** Django Forms se encarga de validar los datos ingresados por el usuario según los tipos de campo definidos.
- **Generación de HTML:** Puedes renderizar fácilmente el formulario en tu plantilla HTML.
- **Seguridad:** Incluye protección CSRF de forma sencilla.
- **Reutilización:** Puedes reutilizar tus formularios en diferentes vistas.