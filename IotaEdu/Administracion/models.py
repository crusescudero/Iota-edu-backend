from django.db import models

# Create your models here.

class Usuario (models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  direccion = models.CharField(max_length=50)
  edad = models.IntegerField()
  email= models.IntegerField()

class Curso (models.Model):
  codigo = models.CharField(max_length=10)
  precio = models.IntegerField()
  duracion = models.CharField(max_length=50)