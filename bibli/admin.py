from django.contrib import admin
from .models import Autor, Editorial, Libro

# Register your models here.

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)

#Para hacer autores y editoriales para meterlos en el combobox