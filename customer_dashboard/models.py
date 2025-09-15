
from django.db import models
from authentication.models import CustomUser
from django.utils import timezone
from super_admin_dashboard.models import State, District, LocalBody, LocalBodyCalendar
from django.conf import settings

class CustomerWasteInfo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('collected', 'Collected'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_info')

    full_name = models.CharField(max_length=255, default='', blank=True)
    secondary_number = models.CharField(max_length=15, blank=True, null=True)
    pickup_address = models.CharField(max_length=255, default="")
    landmark = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    localbody = models.ForeignKey(LocalBody, on_delete=models.SET_NULL, null=True)
    ward = models.CharField(max_length=50, null=True, blank=True)
    number_of_bags = models.IntegerField(null=True, blank=True)
    waste_type = models.CharField(max_length=100, null=True, blank=True)
    comments = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=10)

    assigned_collector = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='assigned_waste'
    )
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.localbody}"


class CustomerPickupDate(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    waste_info = models.ForeignKey(
        'CustomerWasteInfo',
        on_delete=models.CASCADE,
        null=True,  # temporarily allow NULLs
        blank=True,
    )
    localbody_calendar = models.ForeignKey(
        LocalBodyCalendar, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "localbody_calendar")
        indexes = []  # prevent Django from auto-creating duplicate indexes

    def __str__(self):
        return f"{self.user.username} - {self.localbody_calendar.date}"