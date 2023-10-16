from django.db import models

# Create your models here.
class vouchers (models.Model):
    
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
    observacion = models.CharField('Observacion',max_length=50, blank=True)
    estado = models.CharField('Estado',max_length=1, choices=EST_CHOICES,blank=True)
    tipo_pago = models.CharField('Tipo de pago',max_length=1, choices=TIP_CHOICES, blank=True)
    nombre_quien_paga = models.CharField ('Nombre de la persona que paga', max_length=30, blank=True)



    class Meta:
        verbose_name = 'Comprobante'
        verbose_name_plural = 'Comprobantes del club'
        ordering = ['fecha_comprobante']

    def __str__(self):
        return f'Comprobante {self.id} - {self.fecha_comprobante} - {self.get_estado_display()} - {self.get_tipo_pago_display()}'