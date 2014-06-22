from django.contrib import admin
from apps.races.models import RaceEvent, GeneralClassification, Stage, StageResult

admin.site.register(RaceEvent)
admin.site.register(GeneralClassification)
admin.site.register(Stage)
admin.site.register(StageResult)
