# from django import forms
# from .models import CustomerWasteInfo
#
# class CustomerWasteInfoForm(forms.ModelForm):
#     class Meta:
#         model = CustomerWasteInfo
#         fields = ['municipality', 'ward', 'building_no', 'street_name', 'pincode', 'description']







#
# #
# # customer_dashboard/forms.py
# from django import forms
# from .models import CustomerWasteInfo
#
#
# class CustomerWasteInfoForm(forms.ModelForm):
#     pickup_slot = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         label="Confirm your slot"
#     )
#
#     class Meta:
#         model = CustomerWasteInfo
#         exclude = ['user', 'assigned_collector', 'status', 'created_at']
#
#         widgets = {
#             'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
#             'secondary_number': forms.TextInput(attrs={'placeholder': 'Secondary Number (Optional)'}),
#             'pickup_address': forms.Textarea(attrs={'placeholder': 'Pick Up Address & Land Mark', 'rows': 3}),
#             'landmark': forms.TextInput(attrs={'placeholder': 'Land Mark'}),
#             'state': forms.TextInput(attrs={'placeholder': 'State'}),
#             'district': forms.TextInput(attrs={'placeholder': 'District'}),
#             'municipality': forms.TextInput(attrs={'placeholder': 'Corporation/Municipality/Panchayat'}),
#             'ward': forms.TextInput(attrs={'placeholder': 'Ward Number'}),  # FIXED: match model field
#             'number_of_bags': forms.NumberInput(attrs={'min': 1}),
#             'waste_type': forms.TextInput(attrs={'placeholder': 'Waste Type'}),
#             'comments': forms.Textarea(attrs={'placeholder': 'Comments', 'rows': 2}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)  # Pass logged-in customer
#         super().__init__(*args, **kwargs)
#
#         if user:
#             self.fields['full_name'].initial = user.get_full_name()






# from django import forms
# from .models import CustomerWasteInfo
#
# class CustomerWasteInfoForm(forms.ModelForm):
#     MUNICIPALITY_CHOICES = [
#         ('corporation', 'Corporation'),
#         ('municipality', 'Municipality'),
#         ('panchayat', 'Panchayat'),
#     ]
#
#     municipality = forms.ChoiceField(
#         choices=MUNICIPALITY_CHOICES,
#         label="Corporation / Municipality / Panchayat",
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#
#     pickup_slot = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
#         label="Confirm your slot"
#     )
#
#     class Meta:
#         model = CustomerWasteInfo
#         exclude = ['user', 'assigned_collector', 'status', 'created_at']
#
#         widgets = {
#             'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
#             'secondary_number': forms.TextInput(attrs={'placeholder': 'Secondary Number (Optional)', 'class': 'form-control'}),
#             'pickup_address': forms.Textarea(attrs={'placeholder': 'Pick Up Address & Land Mark', 'rows': 3, 'class': 'form-control'}),
#             'landmark': forms.TextInput(attrs={'placeholder': 'Land Mark', 'class': 'form-control'}),
#             'state': forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}),
#             'district': forms.TextInput(attrs={'placeholder': 'District', 'class': 'form-control'}),
#             'ward_number': forms.TextInput(attrs={'placeholder': 'Ward Number', 'class': 'form-control'}),
#             'number_of_bags': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
#             'waste_type': forms.TextInput(attrs={'placeholder': 'Waste Type', 'class': 'form-control'}),
#             'comments': forms.Textarea(attrs={'placeholder': 'Comments', 'rows': 2, 'class': 'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#
#         if user:
#             self.fields['full_name'].initial = user.get_full_name()













#
# from django import forms
# from .models import CustomerWasteInfo
#
# class CustomerWasteInfoForm(forms.ModelForm):
#     pickup_slot = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         label="Confirm your slot"
#     )
#
#     class Meta:
#         model = CustomerWasteInfo
#         exclude = ['user', 'assigned_collector', 'status', 'created_at']
#
#         widgets = {
#             'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
#             'secondary_number': forms.TextInput(attrs={'placeholder': 'Secondary Number (Optional)'}),
#             'pickup_address': forms.Textarea(attrs={'placeholder': 'Pick Up Address & Land Mark', 'rows': 3}),
#             'landmark': forms.TextInput(attrs={'placeholder': 'Land Mark'}),
#             'state': forms.TextInput(attrs={'placeholder': 'State'}),
#             'district': forms.TextInput(attrs={'placeholder': 'District'}),
#             'municipality': forms.TextInput(attrs={'placeholder': 'Corporation/Municipality/Panchayat'}),
#             'ward': forms.TextInput(attrs={'placeholder': 'Ward Number'}),
#             'number_of_bags': forms.NumberInput(attrs={'min': 1}),
#             'waste_type': forms.TextInput(attrs={'placeholder': 'Waste Type'}),
#             'comments': forms.Textarea(attrs={'placeholder': 'Comments', 'rows': 2}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)  # Pass logged-in customer
#         super().__init__(*args, **kwargs)
#
#         if user:
#             # Auto-fill from User model
#             self.fields['full_name'].initial = user.get_full_name()
#
#             # If you have related profile/customer model
#             if hasattr(user, 'customer_profile'):
#                 profile = user.customer_profile
#                 self.fields['district'].initial = profile.district
#                 self.fields['municipality'].initial = profile.municipality
#                 self.fields['ward'].initial = profile.ward
#                 self.fields['number_of_bags'].initial = profile.number_of_bags
#                 self.fields['waste_type'].initial = profile.waste_type



# customer_dashboard/forms.py
from django import forms
from .models import CustomerWasteInfo

class CustomerWasteInfoForm(forms.ModelForm):
    pickup_slot = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False,
        label="Pickup Slot Date"
    )
    class Meta:
        model = CustomerWasteInfo
        fields = ['district', 'municipality', 'ward', 'number_of_bags', 'waste_type']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Remove 'user' from kwargs before calling super
        super().__init__(*args, **kwargs)




# forms.py
# from django import forms
# from .models import CustomerWasteInfo
#
# class CustomerWasteInfoForm(forms.ModelForm):
#     pickup_slot = forms.DateTimeField(
#         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         label="Confirm your slot"
#     )
#
#     class Meta:
#         model = CustomerWasteInfo
#         exclude = ['user', 'assigned_collector', 'status', 'created_at']
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)  # capture 'user'
#         super().__init__(*args, **kwargs)  # call parent init
#
#         # Optionally pre-fill fields if user exists
#         if self.user:
#             self.fields['full_name'].initial = self.user.get_full_name()
#             if hasattr(self.user, 'customer_profile'):
#                 profile = self.user.customer_profile
#                 self.fields['district'].initial = profile.district
#                 self.fields['municipality'].initial = profile.municipality
#                 self.fields['ward'].initial = profile.ward
#                 self.fields['number_of_bags'].initial = profile.number_of_bags
#                 self.fields['waste_type'].initial = profile.waste_type
#
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if self.user:
#             instance.user = self.user
#         if commit:
#             instance.save()
#         return instance
