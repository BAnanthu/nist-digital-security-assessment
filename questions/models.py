from django.db import models


# Create your models here.


class Levels(models.Model):
    TYPE = (
        ('MS', 'MaturityScore'),
        ('TS', 'ThreatScore')
    )
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=70)
    level_details = models.TextField(blank=True,null=True)
    score_type = models.CharField(choices=TYPE, max_length=2,
                                  default='MS')

    def __str__(self):
        return self.level_name


class Options(models.Model):
    option_id = models.AutoField(primary_key=True)
    level_id = models.ForeignKey(Levels,related_name='option', on_delete=models.CASCADE)
    option = models.TextField()
    details = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.option