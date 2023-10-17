from django.contrib import admin
from .models import voucherspartnersXactivities
# Register your models here.
class voucherspartnersXactivitiesAdmin (admin.ModelAdmin):
    list_display = (
        'id'
        'comprobante',
        'socio',
        'actividad',
    )
    search_fields = ['id','comprobante','socio','actividad']
    list_filter = ['comprobante','socio','actividad',]

admin.site.register(voucherspartnersXactivities,voucherspartnersXactivities)