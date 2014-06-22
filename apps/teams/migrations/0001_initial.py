# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('countries', '0001_initial.py'),
    )

    needed_by = (
        ('races', '0001_initial'),
    )

    def forwards(self, orm):
        # Adding model 'Cyclist'
        db.create_table(u'teams_cyclist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['countries.Country'])),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'teams', ['Cyclist'])

        # Adding model 'Team'
        db.create_table(u'teams_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_index=True)),
        ))
        db.send_create_signal(u'teams', ['Team'])

        # Adding model 'Membership'
        db.create_table(u'teams_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('cyclist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Cyclist'])),
            ('season', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'teams', ['Membership'])


    def backwards(self, orm):
        # Deleting model 'Cyclist'
        db.delete_table(u'teams_cyclist')

        # Deleting model 'Team'
        db.delete_table(u'teams_team')

        # Deleting model 'Membership'
        db.delete_table(u'teams_membership')


    models = {
        u'countries.country': {
            'Meta': {'object_name': 'Country'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'teams.cyclist': {
            'Meta': {'object_name': 'Cyclist'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['countries.Country']"})
        },
        u'teams.membership': {
            'Meta': {'object_name': 'Membership'},
            'cyclist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Cyclist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Team']"})
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team_members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teams.Cyclist']", 'through': u"orm['teams.Membership']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['teams']
