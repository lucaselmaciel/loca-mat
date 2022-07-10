from django import forms
from .models import Pessoa


class PessoaForm(forms.Form):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
        