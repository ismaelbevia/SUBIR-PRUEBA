from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=50, blank=True)
    shor_name=models.CharField('Nombre Corto',max_length=20, unique=True)
    anulate=models.BooleanField('Anulado',default=False)
    
    #COSAS Q APLICAR EN LA BASE DE DATOS
    class Meta:
        verbose_name='Mi Departamento'
        verbose_name_plural ='Areas de la empresa'
        ordering =['id'] #ordenar por num
        unique_together = ('name','shor_name') #NO se puden repetir los dos
        
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name
    
    