# from django import forms
# from .models import WasteCollection
#
# class WasteCollectionForm(forms.ModelForm):
#     photo_data = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     class Meta:
#         model = WasteCollection
#         fields = [
#             'customer', 'municipality', 'ward', 'location', 'building_no',
#             'street_name', 'kg', 'photo'
#         ]


# from django import forms
# from .models import WasteCollection
#
# class WasteCollectionForm(forms.ModelForm):
#     # Captured image in base64 – required
#     photo_data = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     class Meta:
#         model = WasteCollection
#         fields = [
#             'customer', 'municipality', 'ward', 'location', 'building_no',
#             'street_name', 'kg', 'photo'  # photo is optional
#         ]
#         widgets = {
#             'municipality': forms.TextInput(attrs={'required': True}),
#             'ward': forms.TextInput(attrs={'required': True}),
#             'location': forms.TextInput(attrs={'required': True}),
#             'building_no': forms.TextInput(attrs={'required': True}),
#             'street_name': forms.TextInput(attrs={'required': True}),
#             'kg': forms.NumberInput(attrs={'required': True}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         photo = cleaned_data.get('photo')
#         photo_data = self.data.get('photo_data')  # from hidden input (base64)
#
#         # Ensure at least camera capture is provided (we ignore file upload)
#         if not photo_data:
#             raise forms.ValidationError("Please capture a photo using the live camera.")
#
#         return cleaned_data


from django import forms
from .models import WasteCollection


class WasteCollectionForm(forms.ModelForm):
    # Only used to receive base64 data from live camera
    photo_data = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = WasteCollection
        # Removed 'photo' from fields
        fields = [
            'customer', 'municipality', 'ward', 'location', 'building_no',
            'street_name', 'kg'
        ]
        widgets = {
            'municipality': forms.TextInput(attrs={'required': True}),
            'ward': forms.TextInput(attrs={'required': True}),
            'location': forms.TextInput(attrs={'required': True}),
            'building_no': forms.TextInput(attrs={'required': True}),
            'street_name': forms.TextInput(attrs={'required': True}),
            'kg': forms.NumberInput(attrs={'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        photo_data = self.data.get('photo_data')  # base64 from hidden input

        if not photo_data:
            raise forms.ValidationError("Please capture a photo using the camera before submitting.")

        return cleaned_data
