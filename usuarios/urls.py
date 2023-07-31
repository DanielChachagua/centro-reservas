from django.urls import path
from .views import *

app_name = "usuarios"

urlpatterns = [
    path('lista/', PerfilesListView.as_view(),name='lista_usuarios'),
    path('crear/',PerfilCreateView.as_view(),name='crear_perfil'),
    #path('crear/',UserCreateView.as_view())
]