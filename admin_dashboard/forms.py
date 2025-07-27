from django import forms
from authentication.models import CustomUser
from django.contrib.auth.hashers import make_password

# class CustomUserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, required=False)
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'first_name', 'last_name', 'email', 'contact_number', 'password', 'role']
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if password:
#             return make_password(password)
#         return password
