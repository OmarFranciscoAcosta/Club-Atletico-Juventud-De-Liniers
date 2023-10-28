from django import forms
from .models import prices

class PricesForm(forms.ModelForm):
    class Meta:
        model = prices
        exclude = ['user']