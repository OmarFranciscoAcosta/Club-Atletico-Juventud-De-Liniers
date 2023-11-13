from django import forms
from .models import prices, activities

class PricesForm(forms.ModelForm):
    class Meta:
        model = prices
        fields = ['anio', 'mes', 'actividad', 'valor_clase_consulta', 'valor_mensual_fijo', 'valor_mensual_1semana', 'valor_mensual_2semana', 'valor_clase_3semana', 'valor_patindanza', 'valor_patin3semanaescula', 'valor_fichaje_anual', 'valor_libre', 'cuota_social', 'medio_mes', 'mes_impago']
    
    