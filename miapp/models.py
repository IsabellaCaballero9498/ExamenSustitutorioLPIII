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

