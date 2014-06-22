# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('countries', '0001_initial.py'),
        ('teams', '0001_initial.py'),
    )

    def forwards(self, orm):
        # Adding model 'RaceEvent'
        db.create_table(u'races_raceevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['countries.Country'])),
            ('class_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_progress', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
        ))
        db.send_create_signal(u'races', ['RaceEvent'])

        # Adding model 'GeneralClassification'
        db.create_table(u'races_generalclassification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race_event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='general_classifications', to=orm['races.RaceEvent'])),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('cyclist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Cyclist'])),
            ('time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'races', ['GeneralClassification'])

        # Adding model 'Stage'
        db.create_table(u'races_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race_event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stages', to=orm['races.RaceEvent'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('has_results', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'races', ['Stage'])

        # Adding model 'StageResult'
        db.create_table(u'races_stageresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='results', to=orm['races.Stage'])),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('cyclist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Cyclist'])),
            ('time', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sprint_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'races', ['StageResult'])


    def backwards(self, orm):
        # Deleting model 'RaceEvent'
        db.delete_table(u'races_raceevent')

        # Deleting model 'GeneralClassification'
        db.delete_table(u'races_generalclassification')

        # Deleting model 'Stage'
        db.delete_table(u'races_stage')

        # Deleting model 'StageResult'
        db.delete_table(u'races_stageresult')


    models = {
        u'countries.country': {
            'Meta': {'object_name': 'Country'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'races.generalclassification': {
            'Meta': {'object_name': 'GeneralClassification'},
            'cyclist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Cyclist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'race_event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'general_classifications'", 'to': u"orm['races.RaceEvent']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'races.raceevent': {
            'Meta': {'object_name': 'RaceEvent'},
            'class_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['countries.Country']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'races.stage': {
            'Meta': {'object_name': 'Stage'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'has_results': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'race_event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stages'", 'to': u"orm['races.RaceEvent']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'races.stageresult': {
            'Meta': {'object_name': 'StageResult'},
            'cyclist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Cyclist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'sprint_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': u"orm['races.Stage']"}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'teams.cyclist': {
            'Meta': {'object_name': 'Cyclist'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['countries.Country']"})
        }
    }

    complete_apps = ['races']
