from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=20)

