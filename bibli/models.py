from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return(self.username)


class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='autores/', blank=True, null=True)

    def __str__(self):
        return(self.nombre)

class Editorial(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    sitio_web = models.URLField()

    def __str__(self):
        return(self.nombre)

class Prestamo(models.Model):
    libro_prestado = models.ForeignKey('Libro', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    ESTADO_CHOICES = [
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='prestado')

    def __str__(self):
        return "Prestamo del libro " + self.libro_prestado.titulo + " a " + self.usuario.username
    
class Genero(models.Model):
    nombre = models.CharField(max_length=255) 
    deacripcion = models.CharField(max_length=255)

    def __str__(self):
        return(self.nombre)

class Libro(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('en_proceso', 'En proceso de préstamo'),
    ]

    titulo = models.CharField(max_length=255)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=20)
    resumen = models.TextField()
    disponibilidad = models.CharField(max_length=20, choices=DISPONIBILIDAD_CHOICES, default='disponible')
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def __str__(self):
        return(self.titulo)


