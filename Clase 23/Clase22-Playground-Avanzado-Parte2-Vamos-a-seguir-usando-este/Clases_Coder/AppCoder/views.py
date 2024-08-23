from django.shortcuts import render
from .models import Curso
from AppCoder.forms import CursoFormulario, BuscaCursoForm
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, "AppCoder/index.html")

@login_required
def cursos(request):
    return render(request, "AppCoder/cursos.html")

@login_required
def profesores(request):
    return render(request, "AppCoder/profesores.html")

@login_required
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

@login_required
def entregables(request):
    return render(request, "AppCoder/entregables.html")



def form_comun(request):

    if request.method == 'POST':

        curso =  Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "AppCoder/index.html")

    return render(request,"AppCoder/form_comun.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppCoder/buscar_form_con_api.html", {"miFormulario": miFormulario})



    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppCoder/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"AppCoder/registro.html" ,  {"form":form, "msg_register": msg_register})