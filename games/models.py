from django.db import models


class Game(models.Model):
    away_team = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    tv_channel = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["date", "time", "id"]

    def __str__(self):
        return f"{self.away_team} at {self.home_team} ({self.date})"
