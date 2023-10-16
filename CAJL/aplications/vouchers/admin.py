from django.contrib import admin
from .models import vouchers
# Register your models here.
class vouchersAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_comprobante',
        'observacion',
        'estado',
        'tipo_pago',
        'nombre_quien_paga',
    )
    search_fields = ['fecha_comprobante','estado','tipo_pago']
    list_filter = ['estado','tipo_pago']

admin.site.register(vouchers,vouchersAdmin)