from django import forms
from django.forms import ModelForm
from .models import Promocao

class PromocaoForm(ModelForm):
    class Meta:
        model = Promocao
        fields = '__all__'
        exclude = ['favoritos']
        #fields = ['nome', 'cidade', 'uf', 'email'] -> Se quiser usar campos específicos.
        #exclude = ['title'] -> Se quiser excluir algum campo
        widgets = {
            'produto': forms.Select(attrs={'class': 'browser-default'}),
            'loja': forms.Select(attrs={'class':'browser-default'}),
        }


class PromocaoEditForm(ModelForm):
    class Meta:
        model = Promocao
        exclude = ['produto', 'loja', 'favoritos']