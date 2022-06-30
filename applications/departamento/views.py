from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm

from applications.persona.models import Empleado
from .models import Departamento

"""PROYECTO1"""

class DepartamentoListView(ListView):
    template_name= 'departamento/lista.html'
    model = Departamento
    context_object_name='departamentos'
    #paginate_by=4
    #ordering ='id'
    

class NewDepartamentoView(FormView):
    template_name='departamento/new_departamento.html'
    form_class=NewDepartamentoForm
    success_url='/'
    
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        ape = form.cleaned_data['apellidos']
        
        depar=Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
            )
        
        depar.save()
        Empleado.objects.create(first_name=nombre,last_name=ape,job='1',departamento=depar)
        return super(NewDepartamentoView,self).form_valid(form)
    