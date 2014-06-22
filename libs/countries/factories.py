import factory

from .models import Country


class CountryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Country

    name = factory.Sequence(lambda n: 'Country %d' % n)
    abbr = 'AAA'
