from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import TimeStampedModel


# Create your models here.
class Vacancy(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    salary = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    salary_from = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    salary_to = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
