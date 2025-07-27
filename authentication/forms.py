from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import RegexValidator
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    contact_number = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit Indian mobile number starting with 6-9.'
            )
        ]
    )


    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'contact_number', 'password1', 'password2', 'role'
        ]

    def check_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
