from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario
from AppCoder.forms import Buscar


# Create your views here.
def inicio(req):
    return render(req, 'appcoder/index.html')


def cursos(req):
    return render(req, 'appcoder/cursos.html')

def profesores(req):
    return render(req, 'appcoder/profesores.html')

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
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/index.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/curso_formulario_2.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
     return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']

        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:

        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)



