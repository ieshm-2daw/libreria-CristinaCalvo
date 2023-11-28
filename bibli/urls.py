from django.urls import path
from .views import ListaLibros, LibroNuevo, UpdateView, DeleteView, DetallesClass

urlpatterns = [
    path('', ListaLibros.as_view(), name='libros_list'),
	path('nuevo_libro/', LibroNuevo.as_view(), name='nuevo_libro'),
    path('detalles/<int:pk>/', DetallesClass.as_view(), name='detalles'),
    path('actualiza/<int:pk>/', UpdateView.as_view(), name='actualiza_form'),
    path('borra/<int:pk>/', DeleteView.as_view(), name='delete'),
]