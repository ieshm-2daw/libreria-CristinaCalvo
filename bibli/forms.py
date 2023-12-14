from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
      model = Libro
      fields = ['titulo', 'autores', 'editorial','ISBN', 'fecha_publicacion', 'genero', 'resumen', 'disponibilidad', 'portada']


class BuscarLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['genero']
