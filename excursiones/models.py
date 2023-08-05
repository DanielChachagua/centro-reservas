from django.db import models

# Create your models here.
class Excursion(models.Model):
    titulo= models.CharField(max_length=100,verbose_name='titulo')
    descripcion= models.TextField(verbose_name='descripcion')
    precio= models.PositiveIntegerField(verbose_name='precio')
    imagen= models.ImageField(verbose_name='imagen',upload_to='excusion/')
    disponible= models.BooleanField(default=True,verbose_name='disponible')
    
    def __str__(self):
        return self.titulo