from django.urls import path
from .views import *

app_name = "usuarios"

urlpatterns = [
    path('lista/', PerfilesListView.as_view(),name='lista_usuarios'),
    path('crear/',PerfilCreateView.as_view(),name='crear_perfil'),
    path('confirmar/<str:token>',confirmar_mail,name='confirmar_mail'),
    path('modificar/<int:pk>',PerfilUpdateView.as_view(),name='editar_usuario'),
    path('cambiar_pass/<int:pk>',CambiarPassword.as_view(),name='cambiar_password'),
]