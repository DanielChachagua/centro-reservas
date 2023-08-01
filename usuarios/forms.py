from django.forms import ModelForm
from django import forms
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    fecha_nacimiento= forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    telefono= forms.CharField(label='Telefono')

    class Meta:
        model = Perfil
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','telefono','fecha_nacimiento']
#     # Puedes agregar widgets personalizados para los campos si lo deseas
#     widgets = {
#         'token': forms.TextInput(attrs={'placeholder': 'Ingrese el token'}),
#         'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el número de teléfono'}),
#     }
        
    def clean_email(self):
        email_field = self.cleaned_data['email']
        if Perfil.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email_field
      
class ConfirmarMail(forms.Form):
    email= forms.EmailField(max_length=200) 
    
    def clean_email(self):
        email_field = self.cleaned_data['email']
        email=Perfil.objects.filter(email=email_field)
        
        if not email.exists():
            raise forms.ValidationError('El correo electrónico no está registrado')
        elif email.activo==False:
            raise forms.ValidationError('La cuenta a la que pertenece su correo no está activada.\n Por favor, revise su correo.')
        return email_field           
