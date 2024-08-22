# from django.shortcuts import render
# from .models import Curso
# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import login, logout, authenticate

# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
#         print(form)
#         if form.is_valid():
#             usuario = form.cleaned_data.get("username")
#             clave = form.cleaned_data.get("password")

#             nombre_usuario = authenticate(username=usuario, password=clave)

#             if usuario is not None:
#                 login (request, nombre_usuario)
#                 return render(request, "AppCoder/index.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
#             else:
#                 form = AuthenticationForm()
#                 return render(request, "AppCoder/login.html", {"mensaje":"Error, datos incorrectos", "form": form})
#         else:
#             return render(request, "AppCoder/index.html", {"mensaje":"Error, formulario inválido"})
    
#     form = AuthenticationForm()

#     return render(request, "AppCoder/login.html", {"form":form})


# class CursoListView(ListView):
#     model = Curso
#     template_name = "AppCoder/Vistas_Clases/curso_list.html"


# class CursoDetalle(DetailView):
#     model = Curso
#     template_name = "AppCoder/Vistas_Clases/curso_detalle.html"


# class CursoCreateView(CreateView):
#     model = Curso
#     template_name = "AppCoder/Vistas_Clases/curso_form.html"
#     success_url = reverse_lazy("List")
#     fields = ["nombre", "camada"]


# class CursoUpdateView(UpdateView):
#     model = Curso
#     template_name = "AppCoder/Vistas_Clases/curso_edit.html"
#     #success_url = reverse_lazy("List")
#     success_url = "/AppCoder/clases/lista/"
#     fields = ["nombre", "camada"]


# class CursoDeleteView(DeleteView):
#     model = Curso
#     success_url = reverse_lazy("List")
#     template_name = "AppCoder/Vistas_Clases/curso_confirm_delete.html"


from django.shortcuts import render  # Para renderizar plantillas HTML
from .models import Curso  # Importa el modelo "Curso" desde tu aplicación
from django.views.generic import ListView  # Para mostrar listas de objetos
from django.views.generic.detail import DetailView  # Para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # Para crear, actualizar y eliminar objetos
from django.urls import reverse_lazy  # Para generar URLs de forma segura

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación

def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":  # Si el formulario fue enviado (método POST)
        form = AuthenticationForm(request, data=request.POST)  # Crea un formulario y lo llena con los datos enviados
        print(form)  # Imprime el formulario en la consola (para depuración)

        if form.is_valid():  # Si el formulario es válido
            usuario = form.cleaned_data.get("username")  # Obtiene el nombre de usuario
            clave = form.cleaned_data.get("password")  # Obtiene la contraseña

            nombre_usuario = authenticate(username=usuario, password=clave)  # Intenta autenticar al usuario

            if nombre_usuario is not None:  # Si la autenticación es exitosa
                login(request, nombre_usuario)  # Inicia la sesión del usuario
                return render(request, "AppCoder/index.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  # Renderiza la plantilla con un mensaje de bienvenida
            else:  # Si la autenticación falla
                form = AuthenticationForm()  # Crea un nuevo formulario vacío
                return render(request, "AppCoder/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza el formulario de login con un mensaje de error
        else:  # Si el formulario no es válido
            return render(request, "AppCoder/index.html", {"mensaje":"Error, formulario inválido"})  # Renderiza la plantilla con un mensaje de error

    form = AuthenticationForm()  # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    return render(request, "AppCoder/login.html", {"form":form})  # Renderiza el formulario de login

class CursoListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Curso  # Modelo con el que trabaja esta vista
    template_name = "AppCoder/Vistas_Clases/curso_list.html"  # Plantilla para renderizar la lista

class CursoDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_detalle.html"

class CursoCreateView(CreateView):
    """
    Vista para crear nuevos cursos a través de un formulario.
    """
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_form.html"
    success_url = reverse_lazy("List")  # URL de redirección después de crear un curso
    fields = ["nombre", "camada"]  # Campos del modelo a mostrar en el formulario

class CursoUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_edit.html"
    # success_url = reverse_lazy("List")
    success_url = "/AppCoder/clases/lista/"  # Otra forma de especificar la URL de redirección
    fields = ["nombre", "camada"]

class CursoDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Curso
    success_url = reverse_lazy("List")  # URL de redirección después de eliminar un curso
    template_name = "AppCoder/Vistas_Clases/curso_confirm_delete.html"  # Plantilla para confirmar la eliminación

