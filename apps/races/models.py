from django.db import models

from apps.teams.models import Cyclist
from libs.countries.models import Country


CLASS_TYPE_CHOICES = (
    ('UWT', 'UWT'),
    ('2.1', '2.1'),
    ('2.2', '2.2'),
    ('CN', 'CN'),
    ('1.HC', '1.HC'),
    ('2.HC', '2.HC'),
    ('CC', 'CC'),
    ('1.2', '1.2'),
    ('1.1', '1.1'),

)


class RaceEvent(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.ForeignKey(Country)
    class_type = models.CharField(max_length=50, choices=CLASS_TYPE_CHOICES)
    in_progress = models.BooleanField(default=False)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class GeneralClassification(models.Model):
    race_event = models.ForeignKey(RaceEvent, related_name='general_classifications')
    rank = models.IntegerField(default=-1)
    cyclist = models.ForeignKey(Cyclist)
    time = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return '%s was %s in %s' % (
            self.cyclist,
            self.rank,
            self.race_event,
        )


class Stage(models.Model):
    race_event = models.ForeignKey(RaceEvent, related_name='stages')
    name = models.CharField(max_length=255)
    date = models.DateField()
    url = models.URLField(max_length=500)
    has_results = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StageResult(models.Model):
    stage = models.ForeignKey(Stage, related_name='results')
    rank = models.IntegerField(default=-1)
    cyclist = models.ForeignKey(Cyclist)
    time = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    sprint_points = models.IntegerField(default=0)

    def __str__(self):
        return '%s was %s in %s' % (
            self.cyclist,
            self.rank,
            self.stage,
        )
