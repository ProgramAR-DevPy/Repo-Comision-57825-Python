from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm, UserRegisterForm
from users.models import Imagen
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



# Create your views here.
def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppCoder/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

# Vista de registro
def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppCoder/index.html")
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


@login_required  # Decorador que requiere que el usuario esté autenticado (logueado) para acceder a esta vista
def editar_perfil(request):
    # Obtiene la instancia del usuario actualmente autenticado a partir de la solicitud (request)
    usuario = request.user

    if request.method == 'POST':  # Verifica si la solicitud es un envío de formulario (método POST)
        # Crea una instancia del formulario UserEditForm, llenándolo con los datos enviados en la solicitud (request.POST y request.FILES) 
        # y utilizando la instancia del usuario actual como base para la edición
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():  # Verifica si los datos del formulario son válidos según las reglas definidas en el formulario
            # Si se ha proporcionado una nueva imagen en el formulario
            if miFormulario.cleaned_data.get('imagen'):
                # Si el usuario ya tiene una imagen asociada (existe un objeto Imagen para este usuario)
                if Imagen.objects.filter(user=usuario).exists():
                    # Actualiza la imagen existente con la nueva imagen del formulario
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()  # Guarda los cambios en el objeto Imagen
                else:
                    # Si el usuario no tiene una imagen asociada, crea un nuevo objeto Imagen 
                    # y lo asocia al usuario actual
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()  # Guarda el nuevo objeto Imagen en la base de datos

            # Guarda los cambios en los datos del usuario (incluyendo cualquier otro campo editado en el formulario)
            miFormulario.save()

            # Renderiza la plantilla "AppCoder/index.html" y la devuelve como respuesta
            return render(request, "AppCoder/index.html")

    else:  # Si la solicitud es un GET (carga inicial de la página)
        # Crea una instancia del formulario UserEditForm, prellenándolo con los datos del usuario actual
        miFormulario = UserEditForm(instance=usuario)

    # Renderiza la plantilla "users/editar_usuario.html", pasando el formulario y la instancia del usuario como contexto
    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")