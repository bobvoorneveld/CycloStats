from apps.teams.models import Cyclist, Team, Membership
from libs.countries.models import Country


def get_cyclist(name, team_abbr, team_name, country_abbr, year):
    country, created = Country.objects.get_or_create(abbr=country_abbr)
    cyclist, created = Cyclist.objects.get_or_create(name=name.title(), nationality=country)
    team, created = Team.objects.get_or_create(abbr=team_abbr, name=team_name.title())
    Membership.objects.get_or_create(team=team, cyclist=cyclist, season=year)
    return cyclist
