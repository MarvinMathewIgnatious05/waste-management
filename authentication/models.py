from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        (0, 'Customer'),
        (1, 'Waste Collector'),
        (2, 'Admin'),
    )

    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return '{}'.format(self.username)



