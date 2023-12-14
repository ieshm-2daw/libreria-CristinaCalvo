from django.contrib import admin
from .models import Autor, Editorial, Libro, Prestamo, Genero

# Register your models here.

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Genero)

#Para hacer autores, editoriales, genero para meterlos en el combobox