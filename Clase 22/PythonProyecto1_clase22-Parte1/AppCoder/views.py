from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, Buscar, ProfesorFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def inicio(req):
    return render(req, 'appcoder/index.html')


def cursos(req):
    return render(req, 'appcoder/cursos.html')

def profesores(request):
     return render(request, 'appcoder/profesores.html')

def estudiantes(req):
    return render(req, 'appcoder/estudiantes.html')

def entregables(req):
    return render(req, 'appcoder/entregables.html')

def curso_form(req):
    if req.method == 'POST':
      
            curso =  Curso(nombre=req.POST['curso'],camada=req.POST['camada'])
 
            curso.save()
 
            return render(req, "AppCoder/index.html")
 
    return render(req,"AppCoder/curso_formulario.html")

def curso_form_2(request):
 
      if request.method == "POST":
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
                  curso.save()
                  return render(request, "AppCoder/index.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/curso_formulario_2.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
     return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.method == "POST":
        miFormulario = Buscar(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            #cursos = Curso.objects.all()
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"], camada=125)

            return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        miFormulario = Buscar()

    return render(request, "AppCoder/curso_formulario_2.html", {"miFormulario": miFormulario})
    
    
    
def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
 
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
 
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
 
    contexto = {"profesores": profesores}
 
    return render(request, "AppCoder/leerProfesores.html", contexto)


def profesorFormulario(request):  

    print("Entrando en la vista profesorFormulario")  # Mensaje de depuración

    if request.method == 'POST':
        print("Solicitud POST recibida")  # Mensaje de depuración

        miFormulario = ProfesorFormulario(request.POST) 

        if miFormulario.is_valid():
            print("Formulario válido")  # Mensaje de depuración

            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], 
                                email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()

            return render(request, "AppCoder/index.html") 
        else:
            print("Formulario no válido")  # Mensaje de depuración

    else:
        print("Solicitud GET recibida")  # Mensaje de depuración
        miFormulario = ProfesorFormulario()

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

