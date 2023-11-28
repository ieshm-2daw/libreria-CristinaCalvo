from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy



class ListaLibros(ListView):
    model = Libro
    template_name = 'bibli/libros_list.html'


class LibroNuevo(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'bibli/nuevo_libro.html'
    success_url = reverse_lazy('libros_list')

#class LibroNuevo(View):
 #   libros = Libro.objects.all()

  #  def post(self,request):
   #     form = LibroForm(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      return redirect ('nuevo_libro')
       # return render(request, 'bibli/nuevo_libro.html',{'libros': self.libros, 'form': form})
   
    #def get(self, request):
     #   form = LibroForm()
      #  return render(request, 'bibli/nuevo_libro.html', {'form' : form})
    
class DetallesClass(DetailView):
    model = Libro
    template_name = 'bibli/detalles.html'

class UpdateView(UpdateView):
    model = Libro
    form_class = LibroForm #para coger todos los campos sin poner fields
    template_name = "bibli/actualiza.html"
    success_url = reverse_lazy('libro_list')
    

class DeleteView(DeleteView):
    model = Libro
    template_name = "bibli/delete.html"
    success_url = reverse_lazy("libros_list")