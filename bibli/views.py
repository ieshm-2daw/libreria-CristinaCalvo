from typing import Any
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Libro, Prestamo
from .forms import LibroForm, BuscarLibro
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from datetime import date, timedelta
from django.contrib.auth.models import User



class ListaLibros(ListView):
    model = Libro
    template_name = 'bibli/libro_list.html'
    queryset = Libro.objects.filter(disponibilidad="disponible") #filtrado

   # def get_context_data(self, **kwargs: Any) -> dict[str, Any]: #no se toca nada aquí

    #  context = super().get_context_data(**kwargs) #contexcto

    #  context['libros_disponibles'] = Libro.objects.filter(disponibilidad="disponible") #filtro
    #  context['libros_prestados'] = Libro.objects.filter(disponibilidad="prestado") #otra forma de hacerlo dos filtros

    #   return context

class LibroNuevo(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'bibli/nuevo_libro.html'
    success_url = reverse_lazy('libro_list')

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
    success_url = reverse_lazy("libro_list")



class RealizarPrestamo(View):
    template_name = "bibli/prestamo.html"

    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, self.template_name, {'libro': libro})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        fecha_prestamo = date.today()
        fecha_devolucion = fecha_prestamo + timedelta(days=30)
        usuario1 = request.user

        prestamo = Prestamo.objects.create(libro_prestado=libro, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion, usuario = usuario1, estado = "prestado")
        prestamo.save()

        libro.disponibilidad = 'prestado'   
        libro.save() 
        return redirect('libro_list')
    

class RealizarDevolucion(View):
    template_name = "bibli/devolucion.html"

    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, self.template_name, {'libro': libro})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        prestamo_anterior = get_object_or_404(Prestamo, libro_prestado=libro, usuario=request.user, estado='prestado') #cogemos prestamo por su libro usuario y estado.
        fecha_prestamo = prestamo_anterior.fecha_prestamo
        fecha_devolucion = date.today()

        prestamo_anterior.fecha_prestamo = fecha_prestamo
        prestamo_anterior.fecha_devolucion = fecha_devolucion
        prestamo_anterior.estado = 'devuelto'
        prestamo_anterior.save()

        libro.disponibilidad = 'disponible'   
        libro.save() 
        return redirect('libro_list')
    

class MisLibros(ListView):
    model = Prestamo
    template_name = "bibli/mislibros.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['prestamo_prestado'] = Prestamo.objects.filter(usuario=self.request.user, estado='prestado') 
        context['prestamo_devuelto'] = Prestamo.objects.filter(usuario=self.request.user, estado='devuelto') 
        return context
    
class FiltraGenero(ListView):
    template_name = 'bibli/genero_list.html'
    form_class = BuscarLibro
    model= Libro
    success_url = reverse_lazy('genero_list')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.GET) #BuscarLibros que sería nuestro get(solicitud)
        context['form'] = form #Se visualiza nuestro formulario

        if form.is_valid():
            genero = form.cleaned_data.get('genero') #Tomamos lo que sería lo que haya en el campo de genero de forma limpia(validos)
            context['libros_genero'] = Libro.objects.filter(genero=genero, disponibilidad='disponible') 
        return context
    



class PanelContadores(ListView):
    template_name = 'bibli/panel.html'
    model= Libro
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['prestado'] = Libro.objects.filter(disponibilidad="prestado")
        context['cont_prestado'] = len(context['prestado'])

        context['disponible'] = Libro.objects.filter(disponibilidad="disponible")
        context['cont_disponible'] = len(context['disponible'])
   
        context['ndevueltos'] = Prestamo.objects.filter(estado="prestado", fecha_devolucion__lte = date.today())

        return context
    
        

        #cont = 0
        #for libro in context['prestado']:
        #    cont = cont + 1
        #    context['cont'] = cont
        #return context
    

    
    