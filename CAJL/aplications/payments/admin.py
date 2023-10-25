from django.contrib import admin
from .models import payments, partners
from django.db.models import Max

# Register your models here.
class paymentsAdmin (admin.ModelAdmin):
    list_display = (
        'comprobante',
        'fecha_pago',
        'monto_pago',
    )
    search_fields = ['id','fecha_pago','monto_pago']
    list_filter = ['fecha_pago', 'fecha_pago']
admin.site.register(payments,paymentsAdmin)