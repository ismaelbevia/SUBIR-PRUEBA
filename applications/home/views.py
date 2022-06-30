from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView

#import models
from .models import Prueba

from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'
    
    
class PruebaListView(ListView):
    template_name = 'home/lista.html'
    #model = 
    queryset = ['0','10','20','30']
    context_object_name='listaNumeros'
    
    
class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name='lista'
    
    """
class PruebaCreate(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    fields = ['titulo','subtitulo','cantidad']
    """
    
class PruebaCreate(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    #fields = ['titulo','subtitulo','cantidad']
    form_class=PruebaForm
    success_url ='/'
    
    
    
    
    
    