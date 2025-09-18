from django import forms
from authentication.models import CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'role',  # Admin can update role
        ]



from customer_dashboard.models import CustomerWasteInfo

class WasteProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerWasteInfo
        fields = [
            "full_name",
            "secondary_number",
            "pickup_address",
            "landmark",
            "pincode",
            "state",
            "district",
            "localbody",
            "ward",
            "waste_type",
            "number_of_bags",
        ]
