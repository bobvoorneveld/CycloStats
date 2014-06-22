# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    needed_by = (
        ('races', '0001_initial'),
        ('teams', '0001_initial'),
    )

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'countries_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'countries', ['Country'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'countries_country')


    models = {
        u'countries.country': {
            'Meta': {'object_name': 'Country'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['countries']
