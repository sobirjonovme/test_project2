import datetime

from django.db import models

from apps.common.models import TimeStampedModel
from apps.task5.models import League, Player, Team


class Match(TimeStampedModel):
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name="home_team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name="away_team")
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()
    match_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

    @classmethod
    def get_todays_matches(self):
        return Match.objects.filter(match_date__date=datetime.date.today(), is_finished=False)

    @classmethod
    def get_old_matches(self):
        return Match.objects.filter(is_finished=True)


class MatchResult(TimeStampedModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    goals = models.IntegerField()
    goals_against = models.IntegerField()
    point = models.IntegerField()

    is_home = models.BooleanField(default=False)
    is_win = models.BooleanField(default=False)
    is_draw = models.BooleanField(default=False)
    is_lose = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team} result in {self.match}"


class Goal(TimeStampedModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True, blank=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    minute = models.IntegerField()
    is_penalty = models.BooleanField(default=False)
    is_assist = models.BooleanField(default=False)
    in_extra_time = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player} goal in {self.match}"
