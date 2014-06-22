from django.db import models

from libs.countries.models import Country


class Cyclist(models.Model):
    name = models.CharField(max_length=255)
    nationality = models.ForeignKey(Country)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    abbr = models.CharField(max_length=3, db_index=True, null=True)
    team_members = models.ManyToManyField(Cyclist, through='Membership', verbose_name='teammembers')

    def __str__(self):
        return self.name


class Membership(models.Model):
    team = models.ForeignKey(Team)
    cyclist = models.ForeignKey(Cyclist)
    season = models.PositiveSmallIntegerField()
