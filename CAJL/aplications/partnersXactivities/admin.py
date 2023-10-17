from django.contrib import admin
from .models import partnerXactivities

# Register your models here.
class partnerXactivitiesAdmin (admin.ModelAdmin):
    list_display = (
        'fecha_inscripcion',
        'socio',
        'actividad',
        'activo',

    )
    search_fields = ('fecha_inscripcion','socio','actividad','activo',)
    list_filter = ('fecha_inscripcion','socio','actividad','activo',)

admin.site.register(partnerXactivities,partnerXactivitiesAdmin)