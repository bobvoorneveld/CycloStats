from lxml import html

from .models import StageResult, GeneralClassification
from apps.teams.functions_cyclist import get_cyclist


def get_stage_results(stage, response):
    doc = html.fromstring(response)

    bread_crumbs = doc.xpath("//div[@class='subtitlered']")[0]
    stage_name_list = bread_crumbs.xpath("text()")[0].strip('\t\n\r').splitlines()
    name = ' '.join([part_name.strip('\t\n\r') for part_name in stage_name_list])
    stage.name = name
    stage.save()

    table = doc.xpath("//table[@class='datatable']")[0]
    rows = table.getchildren()

    best_time = None

    # Store the results
    stage_results = []
    for row in rows:
        cells = row.getchildren()
        try:
            time_string = cells[5].text
            if time_string:
                if time_string.strip() == '':
                    time = -1
                else:
                    if best_time is not None:
                        time = best_time + get_time_in_seconds(time_string.strip())
                    else:
                        time = best_time = get_time_in_seconds(time_string.strip())
            try:
                rank = int(cells[0].text.strip())
            except ValueError:
                rank = -1
            name = cells[1].text.strip()
            country = cells[2].text.strip()
            team_abbr = cells[3][1].text
            team_name = cells[3][1].get('title')
            cyclist = get_cyclist(
                name=name.title(),
                team_abbr=team_abbr,
                team_name=team_name,
                country_abbr=country,
                year=stage.date.year,
            )
            sr = StageResult(
                rank=rank,
                cyclist=cyclist,
                stage=stage,
                time=time,
            )
            stage_results.append(sr)
        except IndexError:
            pass

    # Create all the results at once.
    StageResult.objects.bulk_create(stage_results)

    # Return al the results.
    return stage_results


def get_time_in_seconds(time):
    """
    Returns a time like string to seconds integer.

    Args:
        time (str): time like string.

    Returns:
        int: time in seconds.
    :return:
    """
    time = time.replace('+', '')
    time_list = time.split(':')
    time_list.reverse()
    total_time = 0
    factor = 1
    for time in time_list:
        try:
            total_time += int(time) * factor
            factor *= 60
        except ValueError:
            return None
    return total_time


def get_general_classifications(event, response):
    doc = html.fromstring(response)
    table = doc.xpath("//table[@class='datatable']")[0]
    rows = table.getchildren()

    best_time = None

    # Remove all the classifications
    GeneralClassification.objects.filter(race_event=event).delete()

    # Store classifications.
    gcs = []

    for row in rows:
        cells = row.getchildren()
        try:
            try:
                rank = int(cells[0].text.strip())
            except ValueError:
                rank = -1

            time_string = cells[5].text
            if time_string:
                if time_string.strip() == '':
                    time = -1
                else:
                    if best_time is not None:
                        time = best_time + get_time_in_seconds(time_string)
                    else:
                        time = best_time = get_time_in_seconds(time_string)
            name = cells[1].text.strip()
            country = cells[2].text.strip()
            team_abbr = cells[3][1].text
            team_name = cells[3][1].get('title')
            cyclist = get_cyclist(
                name=name.title(),
                team_abbr=team_abbr,
                team_name=team_name,
                country_abbr=country,
                year=event.end_date.year,
            )
            gc = GeneralClassification(
                rank=rank,
                cyclist=cyclist,
                race_event=event,
                time=time,
            )
            gcs.append(gc)
        except IndexError:
            pass

    # Bulk create all the classifications at once.
    GeneralClassification.objects.bulk_create(gcs)

    # Return al the results.
    return gcs
