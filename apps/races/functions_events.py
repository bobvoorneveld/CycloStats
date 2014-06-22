import datetime

from lxml import html

from .models import RaceEvent, Stage
from libs.countries.models import Country


def get_events(response):
    """
    Get all the events from the response.

    It will create or find the race and saves it to the database.

    Args:
        response (string): An utf-8 encoded string with the UCI website.

    Returns:
        list of events.
    """
    # Find the table with al the races.
    doc = html.fromstring(response)
    table = doc.xpath("//table[@class='datatable']")[0]

    # Store all events.
    events = []

    # For each row, try to parse the data into a event.
    rows = table.getchildren()
    for row in rows:
        cells = row.getchildren()

        # Try to get the data out, assume it fails.
        try:
            name = cells[1][0].text.strip()
            country_abbr = cells[2].text
            class_type = cells[3].text
            url = cells[1].getchildren()[0].get('href')

            # Check if the event still takes place.
            in_progress = False
            try:
                progress_text = cells[1][0][0]
                in_progress = True
            except IndexError:
                pass

            # Datetime only accepts Ascii string.
            date = cells[0][0].text.strip()
            date = date.encode('ASCII', 'ignore')
            try:
                # One day event.
                start_date = datetime.datetime.strptime(date, '%d%b%Y')
                end_date = start_date
            except ValueError:
                # Multi day event.
                start_string = date[0:5] + date[11:]
                start_date = datetime.datetime.strptime(start_string, '%d%b%Y')
                end_string = date[6:]
                end_date = datetime.datetime.strptime(end_string, '%d%b%Y')

            # Find country for this RaceEvent.
            country, created = Country.objects.get_or_create(abbr=country_abbr)

            # Create RaceEvent.
            race_event, created = RaceEvent.objects.get_or_create(
                start_date=start_date,
                end_date=end_date,
                name=name,
                country=country,
                class_type=class_type,
                url=url,
            )
            race_event.in_progress = in_progress
            race_event.save()
            events.append(race_event)
        except IndexError:
            pass

    # Return events.
    return events


def get_stages_for_event_from_response(event, response):
    """
    Create or find stages from an event. Also retreive url for general classification.

    Args:
        event (Event): Event object.
        response (str): UCI html page.

    Returns:
        list of stages
        general_classification_url
    """
    doc = html.fromstring(response)
    bread_crumbs = doc.xpath("//div[@class='crumblepad']")[0]
    event_name_list = bread_crumbs.xpath("text()")[-1:][0].splitlines()
    event_name = event_name_list[1].strip('\t')
    event.name = event_name
    event.save()
    table = doc.xpath("//table[@class='datatable']")[0]

    # Store info
    general_classification_url = None
    stages = []

    # For each row, try to parse the data into a event.
    rows = table.getchildren()
    for row in rows:
        cells = row.getchildren()

        # Try to get the data out.
        try:
            # Datetime only accepts Ascii string.
            date = cells[0][0].text.strip()
            date = date.encode('ASCII', 'ignore')
            try:
                date = datetime.datetime.strptime(date, '%d%b%Y')
            except ValueError:
                end_string = date[6:]
                date = datetime.datetime.strptime(end_string, '%d%b%Y')

            general_classification = False
            name = cells[1][0].text.strip()
            if name == u'General classification':
                general_classification = True
            url = cells[1][0].get('href')
            if not general_classification:
                stage, created = Stage.objects.get_or_create(
                    race_event=event,
                    date=date,
                    url=url,
                )
                stages.append(stage)
            else:
                general_classification_url = url
        except IndexError:
            pass
    return stages, general_classification_url


def check_if_is_results_page(response):
    """
    Check if UCI page is results page or stage page.

    Args:
        response (str): UCI html page.

    Returns:
        Boolean
    """
    doc = html.fromstring(response)
    table = doc.xpath("//table[@class='datatable']")[0]
    if table[0][1].text.strip() == u'Race':
        return False
    return True
