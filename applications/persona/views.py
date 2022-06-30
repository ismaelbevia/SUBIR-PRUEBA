from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from .models import Empleado

#Formularios
from .forms import EmpleadoForm

"""PROYECTO1"""

class InicioView(TemplateView):
    """Pagina de inicio"""
    template_name='inicio.html'


class ListEmpleadosAdmin(ListView):
    template_name= 'persona/lista_empleados.html'
    model = Empleado
    paginate_by=10
    context_object_name='empleados'
    ordering ='id'
    
    
class ListAllEmpleados(ListView):
    template_name= 'persona/list_all.html'
    #model = Empleado
    paginate_by=4
    ordering ='id'
    
    def get_queryset(self):
        kword=self.request.GET.get("kword",'')
        print (kword)
        lista=Empleado.objects.filter(
            full_name__icontains=kword
        )
        return lista


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name= 'persona/detail_empleado.html'
    context_object_name='detalles'
    
    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context
    
class ListByAreaEmpleado(ListView):
    """Lista Area"""
    template_name= 'persona/list_by_area.html'
    
    def get_queryset(self):
        area=self.kwargs['shorname']
        lista=Empleado.objects.filter(departamento__shor_name= area)
        return lista
    
class ListEmpleadosByKword(ListView):
    """Lista por palabra clave"""
    template_name= 'persona/by_kword.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        kword=self.request.GET.get("kword",)
        print (kword)
        lista=Empleado.objects.filter(first_name=kword)
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name= 'persona/habilidades.html'
    context_object_name='habilidades'
    
    def get_queryset(self):
        empleado=Empleado.objects.get(id=4)
        habilidades=empleado.habilidades.all()  
        return habilidades
    

    
class SuccessView(TemplateView):
    template_name="persona/success.html"
        
class EmpleadoCreateView(CreateView):
    model=Empleado
    template_name="persona/add.html"
    #fields=('__all__')
    #fields=['first_name','last_name','job','departamento','habilidades','avatar']
    form_class= EmpleadoForm
    success_url=reverse_lazy('persona_app:empleados_admin')
    
    #NO ES UNA BUENA FORMA 
    def form_valid(self,form):
        empleado=form.save()
        empleado.full_name=empleado.first_name+' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name= 'persona/update.html'
    fields=['first_name','last_name','job','departamento','habilidades']
    success_url=reverse_lazy('persona_app:empleados_admin')
    
    """ 2 Formas: Cada una con sus ventajas"""
    # Esta antes de validad
    
    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        print("UNO")
        return super().post(request,*args,**kwargs)
    
    
    # Esta despues de validar
    def form_valid(self,form):
        print("DOS")
        return super(EmpleadoUpdateView, self).form_valid(form)
    
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name= 'persona/delete.html'
    success_url=reverse_lazy('persona_app:empleados_admin')
    context_object_name='eliminado'
