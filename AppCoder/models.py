from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre= models.CharField(max_length=40)
    codigo = models.IntegerField()
    fechaElab= models.DateField()
    fechaVenc= models.DateField()

class Locales(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    telefono= models.IntegerField()
    email= models.EmailField()

class Chefs(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=30)

class Reservas(models.Model):
    nombre= models.CharField(max_length=30)
    mesa= models.IntegerField()  
    comensales= models.IntegerField()
    reservado = models.BooleanField()
