from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('membresias/', membresias, name="membresias"),
    path('cliente/', cliente, name="cliente"),
    path('libros/', libros, name="libros"),
    path('autores/', autores, name="autores"),

    path('clienteForm/', clienteForm, name="clienteForm"),
    path('autoresForm/', autoresForm, name="autoresForm"),
    path('librosForm/', librosForm, name="librosForm"),
    path('buscarAutor/', buscarAutor, name="buscarAutor"),
    path('buscar2/', buscar2, name="buscar2"),
]
