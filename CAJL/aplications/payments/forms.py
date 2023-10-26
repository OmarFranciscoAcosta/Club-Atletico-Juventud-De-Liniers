from django import forms
from .models import payments

class PaymentsForm (forms.ModelForm):
    class Meta:
        model = payments
        fields = '__all__'