from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class ListEquip(ListView):
    model = Equipamento
    template_name = 'equipamento_list.html'


class EquipFormView(FormView):
    template_name = 'equipamento/create_equipamento.html'
    form_class = EquipamentoForm
    success_url= '/equipamento/list'

    def form_valid(self, form):
        form.save()      
        return super().form_valid(form)


class UpdateEquip(UpdateView):
    model = Equipamento
    # fields = ['codigo', 'locacao_anterior', 'modelo', 'data_compra']
    template_name = 'equipamento/update_equipamento.html'
    form_class = EquipamentoForm
    success_url = '/equipamento/list'


class DeleteEquip(DeleteView):
    model = Equipamento
    success_url = '/equipamento/list'


class ListModelo(ListView):
    model = Modelos
    template_name = 'modelos_list.html'


class CreateModeloFormView(FormView):
    template_name = 'equipamento/create_modelo.html'
    form_class = ModeloForm
    success_url = '/equipamento/list-modelos'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateModeloFormView(FormView):
    template_name = 'update_modelo.html'
    form_class = ModeloForm
    success_url = '/equipamento/list-modelos'


class DeleteModelo(DeleteView):
    model = Modelos
    success_url = '/equipamento/list-modelos'





