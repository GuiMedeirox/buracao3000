from django.contrib import admin
from django.urls import path 
from .views import *

urlpatterns= [
    path('', index, name="index"),
    path('cadastro-buraco', cadastro_buraco, name="cadastro_buraco"),
    path('administrador', administrador, name="administrador"),
    path('editar/<int:id>', editar, name="editar"),
    path('deletar/<int:id>', deletar, name="deletar")
]