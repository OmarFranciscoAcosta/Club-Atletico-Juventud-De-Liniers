from django.db import models
from CAJL.aplications.vouchers.models import vouchers

# Create your models here.
class payments (models.Model):
    comprobante = models.ForeignKey (vouchers,on_delete=models.CASCADE, blank=True)
    fecha_pago = models.DateField ('Fecha del pago',blank=True)
    monto_pago = models.DecimalField('Monto del pago',max_digits=10, decimal_places=2,blank=True, null=True)
    
    
    
    class Meta:
        verbose_name = 'Pagos'
        verbose_name_plural = 'Pagos del club'
        ordering = ['fecha_pago']

def __str__(self):
        return f'{self.id} - {self.fecha_pago} - {self.monto_pago}'