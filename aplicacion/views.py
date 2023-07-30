from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    return render(request, "aplicacion/base.html")

def membresias(request):
    ctx = {"membresias": Membresias.objects.all()}
    return render(request, "aplicacion/membresias.html", ctx)

def libros(request):
    ctx = {"libros": Libros.objects.all()}
    return render(request, "aplicacion/libros.html", ctx)

def cliente(request):
    ctx = {"cliente": Cliente.objects.all()}
    return render(request, "aplicacion/cliente.html", ctx)

def autores(request):
    ctx = {"autores": Autores.objects.all()}
    return render(request, "aplicacion/autores.html", ctx)

def clienteForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], dni=request.POST['dni'], email=request.POST['email'], tipo=request.POST['tipo'])
        cliente.save()
        return HttpResponse("Hemos registrado tus datos!")
    return render(request, "aplicacion/clienteForm.html")

def autoresForm(request):
    if request.method == "POST":
        autores = Autores(nombre=request.POST['nombre'], apellido=request.POST['apellido'])
        autores.save()
        return HttpResponse("Hemos registrado tus datos!")
    return render(request, "aplicacion/autoresForm.html")

def librosForm(request):
    if request.method == "POST":
        libros = Libros(nombre=request.POST['nombre'], autor=request.POST['autor'], anio=request.POST['anio'], editorial=request.POST['editorial'])
        libros.save()
        return HttpResponse("Hemos registrado tus datos!")
    return render(request, "aplicacion/librosForm.html")

def buscarAutor(request):
    return render(request, "aplicacion/buscarAutor.html")

def buscar2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        apellido = Autores.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadoAutores.html", 
                      {"nombre":nombre, "apellido":apellido})
    return HttpResponse("No se ingresaron datos para la busqueda")
    

