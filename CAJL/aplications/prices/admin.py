from django.contrib import admin
from .models import prices

# Register your models here.
class pricesAdmin (admin.ModelAdmin):
    list_display = (
        'anio',
        'mes',
        'actividad',
        'valor_clase_consulta',
        'valor_mensual_fijo',
        'valor_mensual_1semana',
        'valor_mensual_2semana',
        'valor_clase_3semana',
        'valor_fichaje_anual',
        'valor_libre',
        'cuota_social',
        'mes_impago',
    )
    search_fields = ['anio','mes','actividad']
    list_filter = ['anio','mes']

admin.site.register(prices,pricesAdmin)