from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
      model = Libro
      fields = ['titulo', 'autores', 'editorial', 'fecha_publicacion', 'genero', 'resumen', 'disponibilidad', 'portada']