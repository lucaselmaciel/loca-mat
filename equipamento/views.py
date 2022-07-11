from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class ListEquip(ListView):
    model = Equipamento
    template_name: 'equipamento_list.html'

class CreateEquip(CreateView):
    model = Equipamento
    fields = ['codigo', 'locacao_anterior', 'modelo', 'data_compra']
    template_name = 'equipamento/create_equipamento.html'
    success_url= '/equipamento/list'

class UpdateEquip(UpdateView):
    model = Equipamento
    fields = ['codigo', 'locacao_anterior', 'modelo', 'data_compra']
    template_name = 'equipamento/update_equipamento.html'
    success_url = '/equipamento/list'

class DeleteEquip(DeleteView):
    model = Equipamento
    success_url = '/equipamento/list'