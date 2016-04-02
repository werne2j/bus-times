# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Stop.stopNum'
        db.delete_column(u'busing_stop', 'stopNum')

        # Adding field 'Stop.coord_x'
        db.add_column(u'busing_stop', 'coord_x',
                      self.gf('django.db.models.fields.FloatField')(default=43.590579),
                      keep_default=False)

        # Adding field 'Stop.coord_y'
        db.add_column(u'busing_stop', 'coord_y',
                      self.gf('django.db.models.fields.FloatField')(default=-84.775928),
                      keep_default=False)

        # Adding field 'Stop.location_notes'
        db.add_column(u'busing_stop', 'location_notes',
                      self.gf('django.db.models.fields.CharField')(default='No additional notes', max_length='500', null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Stop.stopNum'
        db.add_column(u'busing_stop', 'stopNum',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'Stop.coord_x'
        db.delete_column(u'busing_stop', 'coord_x')

        # Deleting field 'Stop.coord_y'
        db.delete_column(u'busing_stop', 'coord_y')

        # Deleting field 'Stop.location_notes'
        db.delete_column(u'busing_stop', 'location_notes')


    models = {
        u'busing.stop': {
            'Meta': {'object_name': 'Stop'},
            'coord_x': ('django.db.models.fields.FloatField', [], {'default': '43.590579'}),
            'coord_y': ('django.db.models.fields.FloatField', [], {'default': '-84.775928'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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