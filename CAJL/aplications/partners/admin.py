from django.contrib import admin
from .models import partners

# Register your models here.
class PartnersAdmin (admin.ModelAdmin):
    list_display = (
        'nombre_completo',
        'dni',
        'fecha_nacimiento',
        'correo',
        'apto_fisico',
        'distrito',
        'localidad',
    )
    search_fields = ('nombre_completo','dni','fecha_nacimiento','correo','distrito','localidad')
    list_filter = ('nombre_completo','dni','distrito','localidad',)

admin.site.register(partners,PartnersAdmin)