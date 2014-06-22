import datetime

import factory

from .models import Stage, RaceEvent, GeneralClassification
from apps.teams.factories import CyclistFactory
from libs.countries.factories import CountryFactory


class RaceEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = RaceEvent

    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    country = factory.SubFactory(CountryFactory)


class StageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Stage

    race_event = factory.SubFactory(RaceEventFactory)
    date = factory.LazyAttribute(lambda o: datetime.datetime.utcnow())


class GeneralClassificationFactory(factory.DjangoModelFactory):
    class Meta:
        model = GeneralClassification

    race_event = factory.SubFactory(RaceEventFactory)
    cyclist = factory.SubFactory(CyclistFactory)
