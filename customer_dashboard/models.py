
from django.db import models
from authentication.models import CustomUser
from django.utils import timezone


class CustomerWasteInfo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('collected', 'Collected'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_info')

    full_name = models.CharField(max_length=255, default='', blank=True)
    secondary_number = models.CharField(max_length=15, blank=True, null=True)
    pickup_address = models.CharField(max_length=255, default="")
    landmark = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    district = models.CharField(max_length=100, default="Unknown")
    municipality = models.CharField(max_length=100, null=True, blank=True)
    ward = models.CharField(max_length=50, null=True, blank=True)
    number_of_bags = models.IntegerField(null=True, blank=True)
    waste_type = models.CharField(max_length=100, null=True, blank=True)
    pickup_slot = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=10)

    assigned_collector = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='assigned_waste'
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.municipality}"
