from typing import Any, Dict
from django import http
from django.db.models.query import QuerySet
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.core.mail import EmailMessage
from .forms import UserRegisterForm, ConfirmarMail, UserUpdateForm
from .models import Perfil
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
import uuid
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
    form_class=UserRegisterForm
    template_name='usuarios/form.html'
    success_url = reverse_lazy('usuarios:lista_usuarios')  # Cambia 'nombre_de_la_url_exitosa' por la URL a la que quieres redirigir
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    #     form.save()
    #     return HttpResponse("¡Perfil creado exitosamente!")

    def send_mail_confirmacion(self,data):
        mensaje={}
        try:
            email= data['email']
            token=data['token']
            url='http://'+self.request.META['HTTP_HOST']+'/usuarios/confirmar/'+str(token)
            nombre_apellido=data['first_name'] +" "+data['last_name']
            asunto="Trabaja con nosotros"
            from_email=settings.EMAIL_HOST_USER
            to=email
            template=render_to_string('emails/confirmar_email.html',{
                'nombre':nombre_apellido,
                'link_confirmacion':url
            })
            message=strip_tags(template)
            send_mail(asunto,message,from_email,[to],html_message=template)
            mensaje['success'] = "Correo de confirmación enviado exitosamente."
        except Exception as e:
            mensaje['error']=str(e)
        return mensaje
    
    def post(self,request,*args,**kwargs):
        try:
            #form= RegisterForm(request.POST)
            form= self.form_class(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                perfil = form.save(commit=False)
                perfil.token=uuid.uuid4()
                perfil.save()
                data['token']=perfil.token
                self.send_mail_confirmacion(data)
                return redirect(self.success_url)
            
            return render(request,self.template_name,{'form':form})
        except Exception as e:
            print(str(e))
           
def confirmar_mail(request,token):
    perfil=get_object_or_404(Perfil,token=token)
    perfil.activo=True
    perfil.token=None
    perfil.save()
    return redirect('usuarios:lista_usuarios')

class PerfilUpdateView(UpdateView):
    model=Perfil
    form_class=UserUpdateForm
    template_name='usuarios/form.html'
    success_url = reverse_lazy('usuarios:lista_usuarios')
    
class CambiarPassword(FormView):
    model = Perfil
    form_class = PasswordChangeForm
    template_name = 'usuarios/cambio_pass.html'
    success_url = reverse_lazy('login') 
    
    def post(self, request, *args, **kwargs):
        try:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                #update_session_auth_hash(request, form.user)
            else:
                return JsonResponse('hola no mundo del form')
            
        except Exception as e:
            return JsonResponse('hola no mundo')
        return JsonResponse('hola mundo') 
    
        