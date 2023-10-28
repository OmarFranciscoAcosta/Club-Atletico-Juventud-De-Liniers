from django import forms
from .models import partners

class PartnerForm(forms.ModelForm):
    class Meta:
        model = partners
        exclude = ['user']