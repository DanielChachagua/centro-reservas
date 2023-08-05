from django.urls import path
from .views import *

app_name = "excursiones"

urlpatterns = [
    path('', contacto,name='contacto'),
]