from django.db import models

from apps.common.models import TimeStampedModel
from apps.task5.models import Country


class Coach(TimeStampedModel):
    name = models.CharField(max_length=100)
    born = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Stadium(TimeStampedModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Team(TimeStampedModel):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="teams/logos/%Y/%m/%d/")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    founded = models.DateField()
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True, blank=True)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True)
    captain = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Player(TimeStampedModel):
    name = models.CharField(max_length=100)
    born = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
