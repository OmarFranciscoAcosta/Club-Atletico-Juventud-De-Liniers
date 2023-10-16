from django.contrib import admin
from .models import activities
# Register your models here.
class ActivitiesAdmin (admin.ModelAdmin):
    list_display = (
        'nombre_actividad',
        'tipo_actividad',
    )
    search_fields = ('nombre_actividad','tipo_actividad')
    list_filter = ('nombre_actividad', 'tipo_actividad')
    
admin.site.register(activities,ActivitiesAdmin)