from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import RegisterForm
from .models import Perfil
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

#Create your views here.
class PerfilesListView(ListView):
    model=Perfil
    template_name='usuarios/listas.html'
    
    #@login_required
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data={'name':'Daniel'}
        return JsonResponse(data)
    
        
    
    #Trae el contenido de la consulta, se suele enviar en ['object_list']
    def get_queryset(self):
        return Perfil.objects.all()
    
    #modifica el contecto a enviar,se suele enviar en ['object_list']
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Hola mundo'
        context['object_list']=Perfil.objects.all()
        return context
    
class PerfilCreateView(CreateView):
    model=Perfil
    form_class=RegisterForm
    template_name='usuarios/crear.html'
    #success_url = reverse_lazy('nombre_de_la_url_exitosa')  # Cambia 'nombre_de_la_url_exitosa' por la URL a la que quieres redirigir

    
    def form_valid(self, form):
        form.save()
        return HttpResponse("¡Perfil creado exitosamente!")


        