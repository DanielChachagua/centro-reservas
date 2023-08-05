from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
import time
# Create your views here.

def contacto(request):
    form=FormularioContacto()
    if request.method=='POST':
        form=FormularioContacto(data=request.POST)
        if form.is_valid():
            nombre=request.POST.get('nombre')
            telefono=request.POST.get('telefono')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            email=EmailMessage('Byte-Force', 'Usuario: {} \nTeléfono: {} \nCorreo: {} \nMensaje: \n\n{}'.format(nombre,telefono,email,contenido),"",['byte.force.devs@gmail.com'],reply_to=[email])
            try:
                email.send()
                time.sleep(1.5)
                return redirect('/home/')
            except:
                return redirect('/contacto/?no_valido/')
    return render(request,'emails/contacto.html',{'form':form})