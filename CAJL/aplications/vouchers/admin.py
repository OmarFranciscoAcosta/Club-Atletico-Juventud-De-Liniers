from django.contrib import admin
from .models import vouchers
# Register your models here.
class vouchersAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_comprobante',
        'socio',
        'actividades_list',
        'observacion',
        'estado',
        'tipo_pago',
        'nombre_quien_paga',
    )
    search_fields = ['fecha_comprobante','estado','tipo_pago']
    list_filter = ['estado','tipo_pago']
    
    
    def actividades_list(self, obj):
        return ", ".join([str(actividad) for actividad in obj.actividades.all()])

    actividades_list.short_description = 'Actividades'  # Define el título en la lista
    

admin.site.register(vouchers,vouchersAdmin)