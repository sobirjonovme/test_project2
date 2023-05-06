from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel


# Create your models here.
class PhoneNumber(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return str(self.phone_number)
