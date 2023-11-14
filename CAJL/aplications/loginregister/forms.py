from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Personaliza el campo de ayuda para los requisitos de contraseña
        self.fields['password1'].help_text = (
            "La contraseña debe contener al menos 8 caracteres, incluyendo letras mayúsculas y minúsculas, "
            "números y caracteres especiales como @, #, $."
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]

class UserDetailsForm(forms.ModelForm):
    last_login = forms.DateTimeField(label='Último inicio de sesión', disabled=True)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    
    class Meta:
        model = User
        fields = ['last_login','username', 'first_name', 'last_name', 'email', 'is_active','is_staff',]
        