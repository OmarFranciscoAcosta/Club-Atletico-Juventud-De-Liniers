from django import forms
from django.forms.widgets import DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django_select2 import forms as s2forms
from .models import partners, activities, location

class PartnerCreateForm(forms.ModelForm):
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
        help_text='Selecciona la fecha de nacimiento en el calendario.',
        required=False 
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

    localidad = forms.ModelChoiceField(
        queryset=location.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=location,
            search_fields=['municipio_nombre__icontains'],
            attrs={'data-minimum-input-length': 0},
        ),
        label='Localidad',
        required=False
    )
    
    class Meta:
        model = partners
        exclude = ['user']
            
        
class PartnerDetailsForm(forms.ModelForm):
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
        help_text='Selecciona la fecha de nacimiento en el calendario.',
        required=False 
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

    localidad = forms.ModelChoiceField(
        queryset=location.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=location,
            search_fields=['municipio_nombre__icontains'],
            attrs={'data-minimum-input-length': 0},
        ),
        label='Localidad',
        required=False
    )
    
    socio_activo = forms.BooleanField(
        label='Socio activo',
        help_text='Indica si el socio debe ser tratado como activo. Desmarque esta opción en lugar de borrar los datos del mismo.',
        required=False,
    )
    
    class Meta:
        model = partners
        exclude = ['user']
