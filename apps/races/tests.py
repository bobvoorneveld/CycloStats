from django.core.management import call_command
from django.test import TestCase

from .factories import StageFactory, RaceEventFactory
from .functions_events import get_events, get_stages_for_event_from_response, check_if_is_results_page
from .functions_stage import get_stage_results, get_general_classifications
from .models import RaceEvent
from .test_data.events import event_response
from .test_data.general_classification import general_response
from .test_data.multi_stage import event_multi_stage_response
from .test_data.stage import stage_response


class RaceTestCase(TestCase):

    def test_generate_events_from_response(self):
        events = get_events(event_response)
        self.assertEqual(RaceEvent.objects.all().count(), 269)
        self.assertEqual(len(events), 269)

    def test_check_if_is_results_page_or_stages_page(self):
        self.assertTrue(check_if_is_results_page(event_multi_stage_response))
        self.assertFalse(check_if_is_results_page(stage_response))

    def test_get_stages_for_event_from_response(self):
        event = RaceEventFactory()
        stages, general_classification = get_stages_for_event_from_response(event, event_multi_stage_response)
        self.assertEqual(len(stages), 9)
        self.assertEqual(event.name, u'Tour de Suisse')
        self.assertEqual(
            general_classification,
            u'/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110'
            u'&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1'
            u'&Detail=1&Ranking=0'
        )

    def test_find_results_from_single_stage(self):
        race = StageFactory()
        self.assertEqual(race.results.count(), 0)
        get_stage_results(race, stage_response)
        self.assertEqual(race.results.count(), 167)

    def test_find_general_classification_from_event(self):
        event = RaceEventFactory()
        self.assertEqual(event.general_classifications.count(), 0)
        get_general_classifications(event, general_response)
        self.assertEqual(event.general_classifications.count(), 176)
        self.assertEqual(event.general_classifications.first().cyclist.name, u'Rui Alberto Faria Da Costa')
        self.assertEqual(event.general_classifications.last().time, -1)
        self.assertEqual(event.general_classifications.get(rank=121).cyclist.name, u'Andrea Palini')

    def test_roadmap(self):
        call_command('pollracedata')
