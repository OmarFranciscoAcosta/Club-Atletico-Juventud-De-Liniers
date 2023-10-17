from django.db import models
from CAJL.aplications.vouchers.models import vouchers
from CAJL.aplications.partners.models import partners
from CAJL.aplications.activities.models import activities

# Create your models here.
class voucherspartnersXactivities (models.Model):
    comprobante = models.ForeignKey(vouchers, on_delete=models.CASCADE,blank=True)
    socio = models.ForeignKey (partners,on_delete=models.CASCADE,blank=True)
    actividad = models.ForeignKey (activities , on_delete=models.CASCADE,blank=True)
    
    
    def __str__(self):
        return f'{self.id} - {self.comprobante} - {self.socio} - {self.actividad}'