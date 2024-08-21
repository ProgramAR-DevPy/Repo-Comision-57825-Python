from AppCoder import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    path('curso-form/', views.curso_form, name='CursoForm'),
    path('curso-form-2/', views.curso_form_2, name='CursoForm2'),
    path('profesorFormulario/', views.profesorFormulario, name='jose'),
    path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    path('leerProfesores/', views.leerProfesores, name= 'leerProfesores'), 
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    
]


