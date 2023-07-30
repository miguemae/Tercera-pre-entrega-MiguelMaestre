from django.contrib import admin
from .models import Libros, Cliente, Membresias, Autores


# Register your models here.
admin.site.register(Libros)
admin.site.register(Cliente)
admin.site.register(Membresias)
admin.site.register(Autores)