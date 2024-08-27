from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserEditForm(UserChangeForm):
    # Esta clase define un formulario para editar la información de un usuario. 
    # Hereda de UserChangeForm, que es un formulario de Django predefinido para modificar usuarios existentes

    password = None  # Desactiva el campo de contraseña en este formulario, 
                      # evitando que los usuarios cambien su contraseña a través de él.

    # Define los campos del formulario con sus respectivas etiquetas
    email = forms.EmailField(label="Ingrese su email:")      # Campo para el correo electrónico, con validación de formato de email
    last_name = forms.CharField(label='Apellido')          # Campo para el apellido
    first_name = forms.CharField(label='Nombre')            # Campo para el nombre

    imagen = forms.ImageField(label="Avatar", required=False)  # Campo para subir una imagen de avatar. 
                                                               # No es obligatorio (required=False)

    class Meta:
        # Esta clase interna proporciona metadatos sobre el formulario
        model = User                # Indica que este formulario está asociado al modelo de usuario de Django
        fields = ['email', 'last_name', 'first_name', 'imagen']  
        # Lista los campos que se incluirán en el formulario (en el orden en que se mostrarán)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        #help_text = {k: "" for k in fields}