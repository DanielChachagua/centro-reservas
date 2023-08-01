from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    pass

class Perfil(User):
    fecha_nacimiento=models.DateField(verbose_name='Fecha_nacimiento')
    telefono=models.CharField(max_length=50,verbose_name='Telefono')
    token=models.UUIDField(null=True,blank=True,editable=True,verbose_name='Token')
    activo=models.BooleanField(default=False, verbose_name='Activo')
    
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'
        
    def __str__(self):
        return super().get_full_name()

@receiver(post_save, sender=Perfil)
def add_user_to_group(sender, instance, created, **kwargs):
    try:
        group1=Group.objects.get(name='Cliente')
    except Group.DoesNotExist:
        group1=Group.objects.create(name='Cliente')
        group2=Group.objects.create(name='Administrador')
    instance.groups.add(group1)      
       