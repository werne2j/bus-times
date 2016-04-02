# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Stop.id'
        db.alter_column(u'busing_stop', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'Stop.id'
        db.alter_column(u'busing_stop', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        u'busing.stop': {
            'Meta': {'object_name': 'Stop'},
            'coord_x': ('django.db.models.fields.FloatField', [], {'default': '43.590579'}),
            'coord_y': ('django.db.models.fields.FloatField', [], {'default': '-84.775928'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'kind_of_stop': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location_notes': ('django.db.models.fields.CharField', [], {'default': "'No additional notes'", 'max_length': "'500'", 'null': 'True', 'blank': 'True'}),
            'shuttle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_of_request': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']