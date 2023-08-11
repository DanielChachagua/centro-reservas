from django.urls import path
from .views import *

app_name = "contacto"

urlpatterns = [
    path('', Contacto.as_view(),name='contacto'),
    path('home/', ContactoHome.as_view(), name='contacto_home'),
]