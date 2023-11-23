from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings


class Biblioteca(models.Model):
    usuario = models.CharField(max_length=200)
    llibro = models.CharField(max_length=200)
    comentario = models.TextField()
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    prestamo =  models.CharField(max_length=200)

    

def publish(self):
    self.save()

def __str__(self):
    return self.usuario