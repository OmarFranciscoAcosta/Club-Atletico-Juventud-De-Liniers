from django import forms
from django.forms.widgets import DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import partners, activities

class PartnerForm(forms.ModelForm):
    actividades = forms.ModelMultipleChoiceField(
        queryset=activities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text=f'<a href="/agregar_actividad/" target="_blank">Agregar actividad</a>'   
    )
    
    fecha_nacimiento = forms.DateField(
    widget=DatePickerInput(options={
        'format': 'DD/MM/YYYY',
        'locale': 'es'
        # otras opciones que desees incluir
    }),
    help_text='Selecciona la fecha de nacimiento en el calendario.'
    )

    fecha_emisión_apto_físico = forms.DateField(
        widget=DatePickerInput(options={
        'format': 'DD/MM/YYYY',
        'locale': 'es'
        # otras opciones que desees incluir
    }),
        help_text='Selecciona la fecha de emisión del apto físico en el calendario.',
        required=False
    )

    fecha_emisión_fichaje = forms.DateField(
        widget=DatePickerInput(options={
        'format': 'DD/MM/YYYY',
        'locale': 'es'
        # otras opciones que desees incluir
    }),
        help_text='Selecciona la fecha de emisión del fichaje en el calendario.',
        required=False
    )



    class Meta:
        model = partners
        exclude = ['user']

        
        
        