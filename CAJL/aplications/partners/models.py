from tkinter import CASCADE
from django.db import models
from CAJL.aplications.location.models import location
from CAJL.aplications.activities.models import activities
from django.contrib.auth.models import User
# Create your models here.



class partners (models.Model):
    
    nombre_completo = models.CharField ('Nombre completo',max_length=50)
    dni = models.IntegerField('DNI')
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    direccion = models.CharField('Dirección', max_length=50)
    
    DISTRICT_CHOICES = location.LOC_CHOICES
    
    
    
    distrito = models.CharField('Distrito',max_length=2, choices=DISTRICT_CHOICES)
    localidad = models.ForeignKey(location, on_delete=models.CASCADE)
    telefono1 = models.CharField('Teléfono 1',max_length=15,blank=True)
    telefono2 = models.CharField('Teléfono 2',max_length=15,blank=True)
    actividades = models.ManyToManyField(activities)
    correo = models.EmailField('Email',max_length=40,blank=True)
    descripcion = models.CharField('Descripción',max_length=50, blank=True)
    apto_fisico = models.BooleanField('Apto físico',default=False)
    fecha_vencimiento_apto_fisico = models.DateField ('Fecha de emisión del apto físico')
    fecha_vencimiento_fichaje = models.DateField ('Fecha de emisión del fichaje')
    compite = models.BooleanField('Fichado',default=False)
    socio_activo = models.BooleanField('Socio activo',default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    @property
    def ultimo_pago(self):
        # Obtener los pagos asociados a este socio con estado '0' o '1' y ordenar por fecha de comprobante en orden descendente
        ultimos_pagos = self.payments_set.filter(estado__in=['0', '1']).order_by('-fecha_comprobante')
        
        if ultimos_pagos.exists():
            # Devolver el mes del primer pago en la lista ordenada
            return ultimos_pagos[0].get_mes_display()
        else:
            # No se encontraron pagos con estado '0' o '1'
            return None
    
    
    
    
    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios del club'
        ordering = ['nombre_completo']
    def __str__(self):
        return f'Socio {self.id} - {self.nombre_completo} - {self.dni}'