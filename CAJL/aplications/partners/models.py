from tkinter import CASCADE
from django.db import models
from CAJL.aplications.location.models import location
from CAJL.aplications.activities.models import activities
# Create your models here.



class partners (models.Model):
    
    nombre_completo = models.CharField ('Nombre completo',max_length=50)
    dni = models.IntegerField('Dni')
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    direccion = models.CharField('Dirección', max_length=50)
    
    DISTRICT_CHOICES = location.LOC_CHOICES
    
    
    
    distrito = models.CharField('Distrito',max_length=2, choices=DISTRICT_CHOICES)
    localidad = models.ForeignKey(location, on_delete=models.CASCADE)
    telefono1 = models.CharField('Telefono 1',max_length=15,blank=True)
    telefono2 = models.CharField('Telefono 2',max_length=15,blank=True)
    actividades = models.ManyToManyField(activities)
    correo = models.EmailField('Email',max_length=40,blank=True)
    descripcion = models.CharField('Descripción',max_length=50, blank=True)
    apto_fisico = models.BooleanField('Apto físico',default=False)
    fecha_vencimiento_apto_fisico = models.DateField ('Fecha de emisión del apto físico',blank=True)
    fecha_vencimiento_fichaje = models.DateField ('Fecha de emisión del fichaje',blank=True)
    compite = models.BooleanField('Fichado',default=False)
    socio_activo = models.BooleanField('Socio activo',default=False)
    
    
    
    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios del club'
        ordering = ['nombre_completo']
    def __str__(self):
        return f'Socio {self.id} - {self.nombre_completo} - {self.dni}'