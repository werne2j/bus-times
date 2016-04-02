# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stop.stopNum'
        db.add_column(u'busing_stop', 'stopNum',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stop.stopNum'
        db.delete_column(u'busing_stop', 'stopNum')


    models = {
        u'busing.stop': {
            'Meta': {'object_name': 'Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_of_stop': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shuttle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stopNum': ('django.db.models.fields.IntegerField', [], {}),
            'time_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_of_request': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']