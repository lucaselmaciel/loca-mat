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