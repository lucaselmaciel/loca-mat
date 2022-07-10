from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class ListEquip(ListView):
    model = Equipamento
    template_name: 'list_equipamento.html'

class CreateEquip(CreateView):
    model = Equipamento
    fields = ['codigo', 'locacao_anterior', 'modelo', 'data_compra']
    template_name = 'create_equipipamento.html'
    success_url= '/equipamento'