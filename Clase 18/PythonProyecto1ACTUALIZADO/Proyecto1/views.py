from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from AppCoder.models import Curso





def saludo(request):
    return HttpResponse("Hola Django - Coder")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")


def dia_de_hoy(request):
    hoy = datetime.now()
    return HttpResponse(f"Hoy es {hoy}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

# Agregamos al encabezado del archivo el import de Template y de Context


def probando_template(request):

    nom = "Alejandro"
    ap = "Pascual"
    
    lista_notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



    diccionario = {"nombre": nom, "apellido": ap, "hoy": datetime.now(), "notas": lista_notas}

    # # Abrimos el archivo html
    # #mi_html = open('C:/Users/Estudiante/Desktop/PythonProyecto1/Proyecto1/template/template1.html')
    # mi_html = open('./proyecto1/template/template1.html')

    # # Creamos el template haciendo uso de la clase Template
    # plantilla = Template(mi_html.read())

    # # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    # mi_html.close()



    # # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    # mi_contexto = Context(diccionario)


    plantilla = loader.get_template('template1.html')
    
    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def agregar_curso(request, nom, cam):
    curso = Curso(nombre=nom, camada=cam)
    curso.save()

    return HttpResponse("Curso agregado")


