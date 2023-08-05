from django.forms import ModelForm
from django import forms
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm

class UserRegisterForm(UserCreationForm):
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
    
class UserUpdateForm(UserChangeForm):
    password=None
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    telefono= forms.CharField(label='Telefono')
    fecha_nacimiento= forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Perfil
        fields = ['username', 'first_name', 'last_name', 'telefono','fecha_nacimiento']

                   
# class UserForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs['autofocus'] = True

#     class Meta:
#         model = Perfil
#         fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image', 'groups'
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese sus nombres',
#                 }
#             ),
#             'last_name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese sus apellidos',
#                 }
#             ),
#             'email': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su email',
#                 }
#             ),
#             'username': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su username',
#                 }
#             ),
#             'password': forms.PasswordInput(render_value=True,
#                                             attrs={
#                                                 'placeholder': 'Ingrese su password',
#                                             }
#                                             ),
#             'groups': forms.SelectMultiple(attrs={
#                 'class': 'form-control select2',
#                 'style': 'width: 100%',
#                 'multiple': 'multiple'
#             })
#         }
#         exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']

#     def save(self, commit=True):
#         data = {}
#         form = super()
#         try:
#             if form.is_valid():
#                 pwd = self.cleaned_data['password']
#                 u = form.save(commit=False)
#                 if u.pk is None:
#                     u.set_password(pwd)
#                 else:
#                     user = User.objects.get(pk=u.pk)
#                     if user.password != pwd:
#                         u.set_password(pwd)
#                 u.save()
#                 u.groups.clear()
#                 for g in self.cleaned_data['groups']:
#                     u.groups.add(g)
#             else:
#                 data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return data