from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import CreateView,ListView,UpdateView, DeleteView
from .models import Excursion
from .forms import ExcursionForm
from django.urls import reverse_lazy
import os

class ExcursionList(ListView):
    model=Excursion
    template_name= 'excursiones/lista.html'
    
class ExcursionCreate(CreateView):
    model= Excursion
    template_name= 'excursiones/form.html'
    form_class= ExcursionForm
    success_url= reverse_lazy('excursiones:lista_excursiones')
    
class ExcursionUpdate(UpdateView):
    model= Excursion
    template_name= 'excursiones/form.html'
    form_class= ExcursionForm
    success_url= reverse_lazy('excursiones:lista_excursiones') 
    
    def form_valid(self, form):
        # Obtenemos la instancia de Excursion que se va a editar
        excursion = self.get_object()

        # Si se ha enviado un archivo de imagen en la solicitud
        # y si hay una imagen anterior, eliminamos la imagen anterior
        if 'imagen' in self.request.FILES and excursion.imagen:
            path_to_delete = excursion.imagen.path
            if os.path.exists(path_to_delete):
                os.remove(path_to_delete)

        # Llamamos al método form_valid() de la clase base para guardar los cambios
        return super().form_valid(form)
    
class ExcursionDelete(DeleteView):
    model= Excursion
    success_url= reverse_lazy('excursiones:lista_excursiones')       
    template_name= 'excursiones/eliminar.html'
    
    def form_valid(self, form):
        # Obtenemos la instancia de Excursion que se va a eliminar
        excursion = self.get_object()

        # Eliminamos los archivos de imagen asociados a la instancia
        # Asegúrate de ajustar el atributo 'imagen' según el nombre de tu campo en el modelo
        if excursion.imagen:
            path_to_delete = excursion.imagen.path
            if os.path.exists(path_to_delete):
                os.remove(path_to_delete)

        # Llamamos al método form_valid() de la clase base para continuar con la eliminación
        return super().form_valid(form)
    
def disponible(request,pk):
    excursion= get_object_or_404(Excursion,pk=pk)
    excursion.disponible = not excursion.disponible
    excursion.save()       
    return redirect('excursiones:lista_excursiones')  