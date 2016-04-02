# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):


        # Renaming column for 'Stop.shuttle' to match new field type.
        db.rename_column(u'busing_stop', 'shuttle_id', 'shuttle')
        # Changing field 'Stop.shuttle'
        db.alter_column(u'busing_stop', 'shuttle', self.gf('django.db.models.fields.CharField')(max_length=200))



    def backwards(self, orm):
        # Adding index on 'Stop', fields ['shuttle']
        db.create_index(u'busing_stop', ['shuttle_id'])

        # Adding model 'Shuttle'
        db.create_table(u'busing_shuttle', (
            ('bus', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'busing', ['Shuttle'])


        # Renaming column for 'Stop.shuttle' to match new field type.
        db.rename_column(u'busing_stop', 'shuttle', 'shuttle_id')
        # Changing field 'Stop.shuttle'
        db.alter_column(u'busing_stop', 'shuttle_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['busing.Shuttle']))

    models = {
        u'busing.stop': {
            'Meta': {'object_name': 'Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_of_stop': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shuttle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_of_request': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']