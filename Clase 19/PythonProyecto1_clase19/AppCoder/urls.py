from AppCoder import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
    
]