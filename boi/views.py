from django.shortcuts import render, redirect
from django.db.models import Q
from boi import forms
from boi import models
from boi.forms import CurralModelForm,  BoiModelForm, LoteModelForm, MedicamentoModelForm
from boi.models import Curral, Lote, Medicamento, Boi
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, ListView

def home(request):
    return render(request, 'home/base.html')

def lista_curral_view(request):
    # Recupera todos os currais ordenados por nome
    currais = models.Curral.objects.all().order_by('nome')

    # Recupera o valor da busca
    search = request.GET.get('search', '').strip()

    # Se há texto na busca, filtra os currais pelo nome ou tipo de curral
    if search:
        currais = currais.filter(
            Q(nome__icontains=search) | 
            Q(curral_type__tipo_curral__icontains=search)
        )

    return render(request, 'curral/listacurral.html', {'currais': currais})

class CurralCreateView(CreateView):
    model = Curral
    form_class = CurralModelForm
    template_name = 'curral/criarcurral.html'
    success_url = '/listacurral/'

class CurralDetailView(DetailView):
    model = Curral
    template_name = 'curral/detalhecurral.html'
    
class CurralUpdateView(UpdateView):
    model = Curral
    form_class = CurralModelForm
    template_name = 'curral/atualizarcurral.html'
    success_url = '/listacurral/'

class CurralDeleteView(DeleteView):
    model = Curral
    template_name = 'curral/deletarcurral.html'
    success_url = '/listacurral/'



def lista_lote_view(request):
    lotes = models.Lote.objects.all().order_by('nome')

    search = request.GET.get('search', '').strip()

    if search:
        lotes = lotes.filter(
            Q(nome__icontains=search) |
            Q(curral__nome__icontains=search)
        )
    
    return render(request, 'lote/listalote.html', {'lotes': lotes})
    
class LoteCreateView(CreateView):
    model = Lote
    form_class = LoteModelForm
    template_name = 'lote/criarlote.html'
    success_url = '/listalote/'

class LoteDetailView(DetailView):
    model = Lote
    template_name = 'lote/detalhelote.html'

class LoteUpdateView(UpdateView):
    model = Lote
    form_class = LoteModelForm
    template_name = 'lote/atualizarlote.html'
    success_url = '/listalote/'
    
class LoteDeleteView(DeleteView):
    model = Lote
    template_name = 'lote/deletarlote.html'
    success_url = '/listalote/'


def lista_boi_view(request):
    bois = models.Boi.objects.all().order_by('brinco')
    
    search = request.GET.get('search', '').strip()
    
    if search:
        # Normalize search input for comparison
        search = search.lower()
        bois = bois.filter(
            Q(brinco__icontains=search) |
            Q(fornecedor__icontains=search) |
            Q(status_boi__tipo_status__icontains=search) |
            Q(lote__nome__icontains=search) |
            Q(data_entrada__icontains=search)
        )
    
    return render(request, 'boi/listaboi.html', {'bois': bois})

class BoiCreateView(CreateView):
    model = Boi
    form_class = BoiModelForm
    template_name = 'boi/criarboi.html'
    success_url = '/listaboi/'

class BoiDetailView(DetailView):
    model = Boi
    template_name = 'boi/detalheboi.html'
        
class BoiUpdateView(UpdateView):
    model = Boi
    form_class = BoiModelForm
    template_name = 'boi/atualizarboi.html'
    success_url = '/listaboi/'

class BoiDeleteView(DeleteView):
    model = Boi
    template_name = 'boi/deletarboi.html'
    success_url = '/listaboi/'



def lista_medicamento_view(request):
    medicamentos = models.Medicamento.objects.all()

    search = request.GET.get('search', '').strip()

    if search:
        search = search.lower()
        medicamentos = medicamentos.filter(
            Q(nome__icontains=search) |
            Q(laboratorio__nome__icontains=search) |
            Q(tipo_medicamento__tipo_medicamento__icontains=search) 
        )
    return render(request, 'medicamento/listamedicamento.html', {'medicamentos': medicamentos})

class MedicamentoCreateView(CreateView):
    model = Medicamento
    form_class = MedicamentoModelForm
    template_name = 'medicamento/criarmedicamento.html'
    success_url = '/listamedicamento/'
    
class MedicamentoDetailView(DetailView):
    model = Medicamento
    template_name = 'medicamento/detalhemedicamento.html'
    
class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    form_class = MedicamentoModelForm
    template_name = 'medicamento/atualizarmedicamento.html'
    success_url = '/listamedicamento/'
    
class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'medicamento/deletarmedicamento.html'
    success_url = '/listamedicamento/'