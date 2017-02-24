from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    hattrick_team_id = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Player(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    keeper = models.IntegerField()
    defending = models.IntegerField()
    playmaking = models.IntegerField()
    winger = models.IntegerField()
    passing = models.IntegerField()
    scoring = models.IntegerField()
    set_pieces = models.IntegerField()

class Change(models.Model):
    SKILL_TYPES = (
        ('keeper', 'keeper'),
        ('defending', 'defending'),
        ('playmaking', 'playmaking'),
        ('winger', 'winger'),
        ('passing', 'passing'),
        ('scoring', 'scoring'),
        ('set_pieces', 'set_pieces'),
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    change_date = models.DateField()
    old_value = models.IntegerField()
    new_value = models.IntegerField()
    skill = models.CharField(max_length=255, choices=SKILL_TYPES)