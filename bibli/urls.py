from django.urls import path
from .views import ListaLibros, LibroNuevo, UpdateView, DeleteView, DetallesClass, RealizarPrestamo, RealizarDevolucion, MisLibros, FiltraGenero, PanelContadores
from . import views

urlpatterns = [
    path('', ListaLibros.as_view(), name='libro_list'),
	path('nuevo_libro/', LibroNuevo.as_view(), name='nuevo_libro'),
    path('detalles/<int:pk>/', DetallesClass.as_view(), name='detalles'),
    path('actualiza/<int:pk>/', UpdateView.as_view(), name='actualiza_form'),
    path('borra/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('realizar_prestamo/<int:pk>/', RealizarPrestamo.as_view(), name='realizar_prestamo'),
    path('realizar_devolucion/<int:pk>/', RealizarDevolucion.as_view(), name='realizar_devolucion'),
    path('mislibros/', MisLibros.as_view(), name='mislibros'),
    path('genero_list/', FiltraGenero.as_view(), name='genero_list'),
    path('panel/', PanelContadores.as_view(), name='panel'),
]
