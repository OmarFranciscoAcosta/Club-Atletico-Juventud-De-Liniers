from django.db import models
from CAJL.aplications.partners.models import partners
from CAJL.aplications.activities.models import activities
from django.contrib.auth.models import User

# Create your models here.
class payments (models.Model):
    
    EST_CHOICES =(
        ('0','Pagado'),
        ('1','Pago Parcial'),
        ('2','Pagado y Confirmado'),
        ('3', 'No Definido'),
    )
    
    TIP_CHOICES =(
        ('0','Efectivo'),
        ('1','Mercado Pago'),
        ('2','Transferencia'),
        ('3','No Definido'),
    )
    
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
    
    
    
    
    fecha_comprobante = models.DateField('Fecha del comprobante', null=True)
    anio = models.IntegerField('Año facturado', blank=True)
    mes = models.CharField('Mes facturado',max_length=2,choices=MES_CHOICES, blank=True)
    socio = models.ForeignKey(partners, on_delete=models.CASCADE)
    actividades = models.ManyToManyField(activities)
    observacion = models.CharField('Observación',max_length=50, blank=True)
    estado = models.CharField('Estado',max_length=1, choices=EST_CHOICES)
    tipo_pago = models.CharField('Tipo de pago',max_length=1, choices=TIP_CHOICES)
    nombre_quien_paga = models.CharField ('Nombre de la persona que paga', max_length=30, blank=True)
    fecha_pago = models.DateField ('Fecha del pago',null=True, blank=True)
    monto_pago = models.DecimalField('Monto del pago',max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos del club'
        ordering = ['-fecha_comprobante']

    def __str__(self):
        return f'Comprobante {self.id} - {self.fecha_comprobante} - {self.get_estado_display()} - {self.get_tipo_pago_display()}'
    
    
    