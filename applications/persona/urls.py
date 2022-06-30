from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print("=========================Persona============================")
    
from . import views

app_name='persona_app'

urlpatterns = [
    path('buscar-empleado/',views.ListEmpleadosByKword.as_view()),
    path('buscar-habilidades/',views.ListHabilidadesEmpleado.as_view()),
    path('add-empleado/',views.EmpleadoCreateView.as_view(),name='empleado_add'),
    path('success/',views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/',views.EmpleadoUpdateView.as_view(),name='modificar_empleado'),
    path('delete-empleado/<pk>/',views.EmpleadoDeleteView.as_view(),name='eliminar_empleado'),
    path('',views.InicioView.as_view(),name='inicio'),
    path('listar-todo-empleados/',views.ListAllEmpleados.as_view(),name='empleados_all'),
    path('ver-empleado/<pk>/',views.EmpleadoDetailView.as_view(),name='empleado_detail'),
    path('listar-by-area/<shorname>/',views.ListByAreaEmpleado.as_view(),name='empleados_area'),
    path('listar-empleados-admin/',views.ListEmpleadosAdmin.as_view(),name='empleados_admin'),

    #path('persona/', DesdeApps),
]