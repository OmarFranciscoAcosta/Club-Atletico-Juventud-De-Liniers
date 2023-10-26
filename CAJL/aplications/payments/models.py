from django.db import models
from CAJL.aplications.partners.models import partners
from CAJL.aplications.activities.models import activities

# Create your models here.
class payments (models.Model):
    
    EST_CHOICES =(
        ('0','Pagado'),
        ('1','No Pagado'),
        ('2','No Definido'),
    )
    
    TIP_CHOICES =(
        ('0','Efectivo'),
        ('1','Tarjeta'),
        ('2','Transferencia'),
        ('3','No Definido'),
    )
    
    
    fecha_comprobante = models.DateField('Fecha del comprobante',blank=True)
    socio = models.ForeignKey(partners, on_delete=models.CASCADE, blank=True)
    actividades = models.ManyToManyField(activities,blank=True)
    observacion = models.CharField('Observacion',max_length=50, blank=True)
    estado = models.CharField('Estado',max_length=1, choices=EST_CHOICES,blank=True)
    tipo_pago = models.CharField('Tipo de pago',max_length=1, choices=TIP_CHOICES, blank=True)
    nombre_quien_paga = models.CharField ('Nombre de la persona que paga', max_length=30, blank=True)
    fecha_pago = models.DateField ('Fecha del pago',blank=True)
    monto_pago = models.DecimalField('Monto del pago',max_digits=10, decimal_places=2,blank=True, null=True)



    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos del club'
        ordering = ['-fecha_comprobante']

    def __str__(self):
        return f'Comprobante {self.id} - {self.fecha_comprobante} - {self.get_estado_display()} - {self.get_tipo_pago_display()}'
    
    
    