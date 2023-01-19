from django.db import models
from datetime import datetime


class Leaderboard(models.Model):
    playername = models.CharField(max_length=63)
    mapname = models.CharField(max_length=31)
    killcount = models.IntegerField()
    damagedealt = models.IntegerField()
    playtime = models.CharField(max_length=15)
    time = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name: 'Leaderboard'
        verbose_name_plural: 'Leaderboards'
