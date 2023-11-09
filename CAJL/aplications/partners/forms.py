from django import forms
from .models import partners, activities

class PartnerForm(forms.ModelForm):
    actividades = forms.ModelMultipleChoiceField(
        queryset=activities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text=f'<a href="/agregar_actividad/" target="_blank">Agregar actividad</a>'   
    )
    
    class Meta:
        model = partners
        exclude = ['user']
        
        
        