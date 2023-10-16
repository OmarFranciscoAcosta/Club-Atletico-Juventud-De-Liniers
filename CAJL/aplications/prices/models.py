from django.db import models
from CAJL.aplications.activities.models import activities
# Create your models here.

class prices (models.Model):
    anio = models.IntegerField ('Año',blank=True)
    mes = models.CharField ('Mes', max_length=20, blank=True)
    actividad = models.ForeignKey(activities, on_delete=models.CASCADE, blank=True)
    valor_clase_consulta = models.DecimalField('Valor de la clase por consulta', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_mensual_fijo = models.DecimalField ('Valor mensual fijo', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_mensual_1semana = models.DecimalField('Valor mensual por 1 vez semana', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_mensual_2semana = models.DecimalField ('Valor mensual por 2 veces a la semana',max_digits=10, decimal_places=2,blank=True, null=True)
    valor_clase_3semana = models.DecimalField('Valor mensual por 3 veces a la semana', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_fichaje_anual = models.DecimalField('Valor del fichaje anual', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_libre = models.DecimalField ('Valor libre', max_digits=10, decimal_places=2,blank=True, null=True)
    cuota_social = models.DecimalField('Cuota Social', max_digits=10, decimal_places=2,blank=True, null=True)
    mes_impago = models.DecimalField('Mes impago', max_digits=10, decimal_places=2,blank=True, null=True)
    
    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios del club'
        ordering = ['anio']