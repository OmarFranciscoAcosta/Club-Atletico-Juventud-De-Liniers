from django import forms
from .models import payments, activities
from bootstrap_datepicker_plus.widgets import DatePickerInput
class PaymentsForm(forms.ModelForm):
    actividades = forms.ModelMultipleChoiceField(
        queryset=activities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text=f'<a href="/agregar_actividad/" target="_blank">Agregar actividad</a>'   
    )
    
    fecha_comprobante = forms.DateField(
    widget=DatePickerInput(options={
        'format': 'DD/MM/YYYY',
        'locale': 'es'
        
    }),
    help_text='Selecciona la fecha de creación del comprobante.'
    )
    
    fecha_pago = forms.DateField(
    widget=DatePickerInput(options={
        'format': 'DD/MM/YYYY',
        'locale': 'es'
        
    }),
    help_text='Selecciona la fecha de pago del comprobante.'
    )
    
    class Meta:
        model = payments
        exclude = ['user']
        
