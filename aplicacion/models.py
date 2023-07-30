from django.db import models


tipos_membresias = (
    ("PLATINUM", "Platinum"),
    ("GOLD", "Gold"),
    ("SILVER", "Silver"),
    ("BRONZE", "Bronze"),
    ("FREE", "Free"),
)


# Create your models here.
class Libros(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    anio = models.IntegerField()
    editorial = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.nombre}, {self.autor} ({self.anio})"
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField()
    tipo = models.CharField(choices=tipos_membresias, max_length=50)
    

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

class Membresias(models.Model):
    tipo = models.CharField(choices=tipos_membresias, max_length=50)
    fechaInicio = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.tipo}"
    
class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"