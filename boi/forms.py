from django import forms
from boi import models
from django.forms.widgets import DateInput

class CurralModelForm(forms.ModelForm):
    
    class Meta:
        model = models.Curral
        fields = '__all__'

class LoteModelForm(forms.ModelForm):

     class Meta:
         model = models.Lote
         fields = ('nome','data_inicio','curral')
    
class BoiModelForm(forms.ModelForm):
    
    class Meta:
        model = models.Boi
        fields = ("brinco",'fornecedor', 'raca', 'sexo', 'peso_entrada', 'data_nascimento', 'data_entrada', 'status_boi', 'lote')

class MedicamentoModelForm(forms.ModelForm):
    
    class Meta:
        model = models.Medicamento
        fields = '__all__'