from django.shortcuts import render
from django.http import HttpResponse


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


