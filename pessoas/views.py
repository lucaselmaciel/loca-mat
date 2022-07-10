from django.shortcuts import render
from . import models
from . import forms 
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class ListarPessoas(ListView):
    model = models.Pessoa
    template_name = 'list_pessoa.html'


class CriarPessoa(CreateView):
    model = models.Pessoa
    fields = ['nome', 'cpf', 'status_atraso_pagamento', 'data_nascimento']
    template_name = 'create_pessoa.html'
    success_url = '/pessoas/list'


class EditarPessoa(UpdateView):
    model = models.Pessoa
    fields = ['nome', 'cpf', 'status_atraso_pagamento', 'data_nascimento']
    template_name = 'update_pessoa.html'
    success_url = '/pessoas/list'


class DeletarPessoa(DeleteView):
    model = models.Pessoa
    success_url = '/pessoas/list'