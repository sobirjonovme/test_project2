from django.db import models
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel


class Country(TimeStampedModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class LeagueType(TimeStampedModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class League(TimeStampedModel):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.CharField(max_length=100)
    league_type = models.ForeignKey(LeagueType, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.year


class Mention(TimeStampedModel):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class News(TimeStampedModel):
    title = models.CharField(max_length=100)
    image = ImageField(upload_to="news/images/%Y/%m/%d/")
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NewsMention(TimeStampedModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
    mention = models.ForeignKey(Mention, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.news} - {self.mention}"
