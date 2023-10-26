from django import forms
from .models import activities

class ActivitiesForm (forms.ModelForm):
    class Meta:
        model = activities
        fields = '__all__'
        