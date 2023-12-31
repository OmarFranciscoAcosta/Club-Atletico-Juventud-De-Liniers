from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class activities (models.Model):
    
    ACTIV_CHOICES =(
        ('0', 'Mensual'),
        ('1', 'Porcentaje'),
        ('2', 'Alquiler'),

    )
    
    nombre_actividad = models.CharField ('Nombre de la actividad',max_length=30)
    tipo_actividad = models.CharField('Tipo de cobro de la actividad',max_length=2, choices=ACTIV_CHOICES, default='0')
    descripcion = models.CharField('Descripción', max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades del club'
        ordering = ['id']
    def __str__(self):
        return f'{self.nombre_actividad}'