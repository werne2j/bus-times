# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Stop.kind'
        db.delete_column(u'busing_stop', 'kind')

        # Deleting field 'Stop.request'
        db.delete_column(u'busing_stop', 'request')

        # Adding field 'Stop.type_of_request'
        db.add_column(u'busing_stop', 'type_of_request',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Stop.kind_of_stop'
        db.add_column(u'busing_stop', 'kind_of_stop',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Stop.kind'
        db.add_column(u'busing_stop', 'kind',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Stop.request'
        db.add_column(u'busing_stop', 'request',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Deleting field 'Stop.type_of_request'
        db.delete_column(u'busing_stop', 'type_of_request')

        # Deleting field 'Stop.kind_of_stop'
        db.delete_column(u'busing_stop', 'kind_of_stop')


    models = {
        u'busing.shuttle': {
            'Meta': {'object_name': 'Shuttle'},
            'bus': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'busing.stop': {
            'Meta': {'object_name': 'Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_of_stop': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shuttle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['busing.Shuttle']"}),
            'time_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_of_request': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']