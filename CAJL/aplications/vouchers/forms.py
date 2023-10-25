from django import forms
from .models import vouchers

class VouchersForm (forms.ModelForm):
    class Meta:
        model = vouchers
        fields = '__all__'