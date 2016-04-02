# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Stop.time'
        db.delete_column(u'busing_stop', 'time')

        # Adding field 'Stop.time_1'
        db.add_column(u'busing_stop', 'time_1',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Stop.time_2'
        db.add_column(u'busing_stop', 'time_2',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Stop.time'
        db.add_column(u'busing_stop', 'time',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Deleting field 'Stop.time_1'
        db.delete_column(u'busing_stop', 'time_1')

        # Deleting field 'Stop.time_2'
        db.delete_column(u'busing_stop', 'time_2')


    models = {
        u'busing.shuttle': {
            'Meta': {'object_name': 'Shuttle'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'busing.stop': {
            'Meta': {'object_name': 'Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'request': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shuttle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['busing.Shuttle']"}),
            'time_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_2': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']