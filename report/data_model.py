from django.db import models

from questions.models import Levels, Options


class MeturityScoringTABLE(models.Model):
    id = models.AutoField(primary_key=True)
    level_id = models.ForeignKey(Levels, on_delete=models.CASCADE)
    option_id = models.ForeignKey(Options, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)


class ThreatScoringTABLE(models.Model):
    id = models.AutoField(primary_key=True)
    level_id = models.ForeignKey(Levels, on_delete=models.CASCADE)
    option_id = models.ForeignKey(Options, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)