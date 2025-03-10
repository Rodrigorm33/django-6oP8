# -*- coding: utf-8 -*-
from django import forms
from .models import Multa

class MultaSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': 'Digite o código ou descrição da infração...'
        })
    )
    gravidade = forms.ChoiceField(
        required=False,
        choices=[('', 'Todas')] + list(Multa.objects.values_list('gravidade', 'gravidade').distinct())
    )
