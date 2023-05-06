from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import TimeStampedModel


class SalaryType(models.TextChoices):
    exact = "exact", "Exact"
    range = "range", "Range"


# Create your models here.
class Vacancy(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    salary = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    salary_from = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    salary_to = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)

    type = models.CharField(max_length=10, choices=SalaryType.choices, default=SalaryType.exact)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.title
