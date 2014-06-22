import gevent
from gevent.queue import Queue, Empty

from django.core.management.base import BaseCommand


from ...functions_events import check_if_is_results_page, get_stages_for_event_from_response, get_events
from ...functions_stage import get_stage_results, get_general_classifications
from ...models import StageResult, Stage
from libs.functions import RequestWrapper


class Command(BaseCommand):
    help = 'Fetches all the race data'

    tasks = Queue()

    def worker(self, name):
        try:
            while True:
                object = self.tasks.get()
                print 'Event worker %s got task' % name
                if isinstance(object, Stage):
                    self.process_stage(object)
                else:
                    self.process_event(object)
        except Empty:
            print 'Event worker %s done' % name

    def process_stage(self, stage):
        if not stage.has_results:
            print 'Getting race results info from stage'
            rw = RequestWrapper(stage.url)
            rw.fetch_url()
            results = get_stage_results(stage, rw.result)
            if len(results):
                stage.has_results = True
                stage.save()
            print 'Fetched %s results for stage %s' % (len(results), stage.name)

    def handle(self, *args, **options):

        # Fetch all events
        print 'Fetch all events from main page'

        # 2014
        # url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&TaalCode=2&StyleID=0&SportID=102' \
        #       '&CompetitionID=-1&EditionID=-1&EventID=-1&GenderID=1&ClassID=1&EventPhaseID=0&Phase1ID=0&Phase2ID=0' \
        #       '&CompetitionCodeInv=1&PhaseStatusCode=262280&DerivedEventPhaseID=-1&SeasonID=486' \
        #       '&StartDateSort=20131006&EndDateSort=20141225&Detail=1&DerivedCompetitionID=-1&S00=-3&S01=2&S02=1' \
        #       '&PageNr0=-1&Cache=8'

        # 2013
        # url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&TaalCode=2&StyleID=0&SportID=102' \
        #       '&CompetitionID=-1&EditionID=-1&EventID=-1&GenderID=1&ClassID=1&EventPhaseID=0&Phase1ID=0&Phase2ID=0' \
        #       '&CompetitionCodeInv=1&PhaseStatusCode=262280&DerivedEventPhaseID=-1&SeasonID=484&StartDateSort=20121004' \
        #       '&EndDateSort=20131218&Detail=1&DerivedCompetitionID=-1&S00=-3&S01=2&S02=1&PageNr0=-1&Cache=8'

        # 2012
        # url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&TaalCode=2&StyleID=0&SportID=102' \
        #       '&CompetitionID=-1&EditionID=-1&EventID=-1&GenderID=1&ClassID=1&EventPhaseID=0&Phase1ID=0&Phase2ID=0' \
        #       '&CompetitionCodeInv=1&PhaseStatusCode=262280&DerivedEventPhaseID=-1&SeasonID=482' \
        #       '&StartDateSort=20110930&EndDateSort=20121021&Detail=1&DerivedCompetitionID=-1&S00=-3&S01=2&S02=1' \
        #       '&PageNr0=-1&Cache=8'

        # 2011
        # url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&TaalCode=2&StyleID=0&SportID=102' \
        #       '&CompetitionID=-1&EditionID=-1&EventID=-1&GenderID=1&ClassID=1&EventPhaseID=0&Phase1ID=0' \
        #       '&Phase2ID=0&CompetitionCodeInv=1&PhaseStatusCode=262280&DerivedEventPhaseID=-1&SeasonID=480' \
        #       '&StartDateSort=20101007&EndDateSort=20111223&Detail=1&DerivedCompetitionID=-1&S00=-3&S01=2&S02=1' \
        #       '&PageNr0=-1&Cache=8'

        # 2010
        # url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&TaalCode=2&StyleID=0&SportID=102' \
        #       '&CompetitionID=-1&EditionID=-1&EventID=-1&GenderID=1&ClassID=1&EventPhaseID=0&Phase1ID=0&Phase2ID=0' \
        #       '&CompetitionCodeInv=1&PhaseStatusCode=262280&DerivedEventPhaseID=-1&SeasonID=478' \
        #       '&StartDateSort=20091002&EndDateSort=20101122&Detail=1&DerivedCompetitionID=-1&S00=-3&S01=2&S02=1' \
        #       '&PageNr0=-1&Cache=8'

        # 2009
        url = 'http://www.uci.infostradasports.com/asp/lib/TheASP.asp?PageID=19004&TaalCode=2&StyleID=0&SportID=102' \
              '&CompetitionID=-1&EditionID=-1&EventID=-1&GenderID=1&ClassID=1&EventPhaseID=0&Phase1ID=0&Phase2ID=0' \
              '&CompetitionCodeInv=1&PhaseStatusCode=262280&DerivedEventPhaseID=-1&SeasonID=476' \
              '&StartDateSort=20081003&EndDateSort=20091208&Detail=1&DerivedCompetitionID=-1&S00=-3&S01=2&S02=1' \
              '&PageNr0=-1&Cache=8'

        rw = RequestWrapper(url)
        rw.fetch_url()
        events = get_events(rw.result)

        print 'Fetch all data for all new events'

        for event in events:
            self.tasks.put(event)

        gevent.joinall([
            gevent.spawn(self.worker, '1'),
            gevent.spawn(self.worker, '2'),
            gevent.spawn(self.worker, '3'),
            gevent.spawn(self.worker, '4'),
            gevent.spawn(self.worker, '5'),
            gevent.spawn(self.worker, '6'),
            gevent.spawn(self.worker, '7'),
            gevent.spawn(self.worker, '8'),
            gevent.spawn(self.worker, '9'),
            gevent.spawn(self.worker, '10'),
        ])

        print 'Number of results: %s' % StageResult.objects.all().count()

    def process_event(self, event):

        if self.check_event_needs_processing(event):
            print 'Getting race info from Event: %s' % event.name
            rw = RequestWrapper(event.url)
            rw.fetch_url()
            if check_if_is_results_page(rw.result):
                print 'Getting results from Event: %s' % event.name
                get_general_classifications(event, rw.result)
                print 'Got results from Event: %s' % event.name
            else:
                print 'Get all the stages for event %s' % event.name
                stages, cl_url = get_stages_for_event_from_response(event, rw.result)
                self.get_results_from_stages(stages)
                self.get_general_classification_results(event, cl_url)

    def get_results_from_stages(self, stages):

        for stage in stages:
            self.tasks.put(stage)

    def get_general_classification_results(self, event, cl_url):
        print 'Getting the general classification results'
        rw = RequestWrapper(cl_url)
        rw.fetch_url()
        results = get_general_classifications(event, rw.result)
        print 'Fetched %s results for the general classification' % len(results)

    def check_event_needs_processing(self, event):
        if event.in_progress or event.general_classifications.count() is 0:
            return True
        else:
            stage = event.stages.order_by('-date').first()
            if not stage:
                return True
            if stage.date < event.end_date:
                return True
