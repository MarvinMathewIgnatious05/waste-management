from django import forms
from .models import CustomerWasteInfo

class CustomerWasteInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerWasteInfo
        fields = ['municipality', 'ward', 'building_no', 'street_name', 'pincode', 'description']
