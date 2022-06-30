from django.db import models

# Create your models here.

#IMPORTAMOS DEPARTAMENTO

from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)
    
    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural ='Habilidades empleados'
        
    def __str__(self):
        return self.habilidad
        

class Empleado(models.Model):
    """MOdelo tablas empleados"""
    first_name=models.CharField('Nombres', max_length=60)
    
    last_name=models.CharField('Apellidos', max_length=60)
    
    full_name= models.CharField('Nombres Completos', max_length=120, blank=True)
    
    JOB_CHOICES=(
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
        )
    
    job=models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    
    departamento= models.ForeignKey(Departamento, on_delete=models.CASCADE) #UNA PERSONA UN DEPARTAMENTO
    avatar=models.ImageField(upload_to='empleado',blank=True,null=True)
    habilidades=models.ManyToManyField(Habilidades) # UNA PERSONA PUEDE TENER VARIAS HABILIDADES
    
    #hoja_vida= RichTextField()
    
    #COSAS Q APLICAR EN LA BASE DE DATOS
    class Meta:
        verbose_name='Mi Empleado'
        verbose_name_plural ='Empleados de la empresa'
        ordering =['id'] #ordenar por num
        
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    
    
    
    
    