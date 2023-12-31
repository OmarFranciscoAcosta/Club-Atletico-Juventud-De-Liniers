from django.db import models
from CAJL.aplications.activities.models import activities
from django.contrib.auth.models import User
# Create your models here.

class prices (models.Model):
    MES_CHOICES =(
        ('0', 'Enero'),
        ('1', 'Febrero'),
        ('2', 'Marzo'),
        ('3', 'Abril'),
        ('4', 'Mayo'),
        ('5', 'Junio'),
        ('6', 'Julio'),
        ('7', 'Agosto'),
        ('8', 'Septiembre'),
        ('9', 'Octubre'),
        ('10', 'Noviembre'),
        ('11', 'Diciembre'),

    )
    
    
    anio = models.IntegerField ('Año', blank=False, null=False, default='2023')
    mes = models.CharField('Mes',max_length=2, choices=MES_CHOICES, default='0', blank=False, null=False)
    actividad = models.ForeignKey(activities, on_delete=models.CASCADE, blank=False, null=False)
    valor_clase_consulta = models.DecimalField('Valor de la clase por consulta', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_mensual_fijo = models.DecimalField ('Valor mensual fijo', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_mensual_1semana = models.DecimalField('Valor mensual por 1 vez a la semana', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_mensual_2semana = models.DecimalField ('Valor mensual por 2 veces a la semana',max_digits=10, decimal_places=2,blank=True, null=True)
    valor_clase_3semana = models.DecimalField('Valor mensual por 3 veces a la semana', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_patindanza = models.DecimalField('Valor mensual de Patin con danza', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_patin3semanaescula = models.DecimalField('Valor mensual de 3 veces por semana de Patín + escuela', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_fichaje_anual = models.DecimalField('Valor del fichaje anual', max_digits=10, decimal_places=2,blank=True, null=True)
    valor_libre = models.DecimalField ('Valor libre', max_digits=10, decimal_places=2,blank=True, null=True)
    cuota_social = models.DecimalField('Cuota Social', max_digits=10, decimal_places=2,blank=True, null=True)
    medio_mes = models.DecimalField('Medio Mes', max_digits=10, decimal_places=2,blank=True, null=True)
    mes_impago = models.DecimalField('Recargo', max_digits=10, decimal_places=2,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios del club'
        ordering = ['-anio']