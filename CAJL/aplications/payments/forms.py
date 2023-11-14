from django import forms
from .models import payments, activities, partners
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django_select2 import forms as s2forms
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
    help_text='Selecciona la fecha de creación del comprobante.',
    label = 'Fecha del comprobante',
    required = True
    )
    
    fecha_pago = forms.DateField(
    widget=DatePickerInput(options={
        'format': 'DD/MM/YYYY',
        'locale': 'es'
        
    }),
    help_text='Selecciona la fecha de pago del comprobante.',
    label = 'Fecha del pago',
    required = True
    )
    
    
    socio = forms.ModelChoiceField(
        queryset=partners.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=partners,
            search_fields=['nombre_completo__icontains'],
            attrs={'data-minimum-input-length': 0},
        ),
        label='Socio',
        required= True
    )
    
    
    class Meta:
        model = payments
        exclude = ['user']
        
