from django.urls import path
from .views import *

app_name = "excursiones"

urlpatterns = [
    path('listar/', ExcursionList.as_view(),name='lista_excursiones'),
    path('crear/',ExcursionCreate.as_view(),name='crear_excursion'),
    path('editar/<int:pk>',ExcursionUpdate.as_view(),name='editar_excursion'),
    path('eliminar/<int:pk>',ExcursionDelete.as_view(),name='eliminar_excursion'),
    path('disponible/<int:pk>',disponible,name='disponible_excursion'),
]