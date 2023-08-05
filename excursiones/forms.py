from django import forms
from .models import Excursion

class ExcursionForm(forms.ModelForm):
    titulo= forms.CharField(max_length=100,label='Título')
    descripcion= forms.CharField(widget=forms.Textarea,label='Descripción')
    precio= forms.IntegerField(min_value=0,label='Precio')
    imagen= forms.ImageField(label='Imagen')
    
    class Meta:
        model= Excursion
        exclude= ('disponible',)
    
    