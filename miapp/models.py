from django.db import models
class Libro(models.Model):
    idlibro = models.IntegerField()
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    fecha = models.DateTimeField()
    stock = models.IntegerField()
    idautores = models.IntegerField()
    ideditorial = models.IntegerField()
    idpais= models.IntegerField()

class Autor(models.Model):
    idautor = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    estado= models.CharField(max_length=1)


class Editorial(models.Model):
    ideditorial = models.IntegerField()
    nombre = models.CharField(max_length=100)
    estado= models.CharField(max_length=1)

class Pais(models.Model):
    idpais = models.IntegerField()
    nombre = models.CharField(max_length=100)
    estado= models.CharField(max_length=1)