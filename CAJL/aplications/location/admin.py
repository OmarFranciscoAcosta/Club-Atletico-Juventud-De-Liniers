from django.contrib import admin
from .models import location
# Register your models here.
class LocationAdmin (admin.ModelAdmin):
    list_display = (
        'municipio_nombre',
        'localidad_nombre',
    )
    search_fields = ('municipio_nombre', 'localidad_nombre')
    list_filter = ('localidad_nombre',)


admin.site.register(location,LocationAdmin)