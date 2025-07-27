from django.db import models
from authentication.models import CustomUser

class CustomerWasteInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_info')

    municipality = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    building_no = models.CharField(max_length=20)
    street_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    description = models.CharField(max_length=200, blank=True, null=True)
    assigned_collector = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL,
                                           related_name='assigned_waste')

    def __str__(self):
        return f"{self.user.username} - {self.municipality}"
