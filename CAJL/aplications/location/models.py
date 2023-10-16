from django.db import models

# Create your models here.
class location (models.Model):
    
    LOC_CHOICES =(
        ('0','Provincia de Buenos Aires'),
        ('1','Ciudad Autónoma de Buenos Aires'),
    )
    
    
    municipio_nombre = models.CharField('Nombre del municipio', max_length=40, blank=True)
    localidad_nombre = models.CharField('Nombre de la localidad', max_length=1, choices=LOC_CHOICES, blank=True)
    
    class Meta: 
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['municipio_nombre']
        
    def __str__(self):
        return f'{self.municipio_nombre}'