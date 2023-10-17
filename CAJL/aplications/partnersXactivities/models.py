from django.db import models
from CAJL.aplications.partners.models import partners
from CAJL.aplications.activities.models import activities

# Create your models here.
class partnerXactivities (models.Model):
    fecha_inscripcion = models.DateField ('Fecha de inscripción',blank=True)
    socio = models.ForeignKey (partners, on_delete=models.CASCADE, blank=True)
    actividad = models.ForeignKey (activities, on_delete=models.CASCADE, blank=True)
    activo = models.BooleanField ('Esta activo?',default=False)
    
    class Meta:
        verbose_name = 'Socio por actividad'
        verbose_name_plural = 'Socios por actividades del club'
        ordering = ['socio']
    def __str__(self):
        return f'{self.id} - {self.socio} - {self.actividad}'