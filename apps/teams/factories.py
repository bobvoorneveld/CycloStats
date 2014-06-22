import factory

from .models import Cyclist
from libs.countries.factories import CountryFactory


class CyclistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Cyclist

    nationality = factory.SubFactory(CountryFactory)
