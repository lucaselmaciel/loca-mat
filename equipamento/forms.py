from django import forms
from .models import *

class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = '__all__'
        widgets = {
            'locacao_anterior': forms.DateInput(attrs={
                'id': 'date',
                'class': 'form-control',
                'data-inputmask': "'alias': 'date'"
            }),
            'data_compra': forms.DateInput(attrs={
                'class': 'form-control',
                'data-inputmask-alias':"datetime",
                'data-inputmask-inputformat': 'dd/mm/aaaa'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelos
        fields = '__all__'
        widgets = {
            'facricacao': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '2010'
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'estado_conservacao': forms.Select(attrs={
                'class': 'form-control'
            })

        }


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacoes
        fields = ['cliente', 'equipamento', 'endereco']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-control'
            }),
            'equipamento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'busca_endereco'
            })
        }