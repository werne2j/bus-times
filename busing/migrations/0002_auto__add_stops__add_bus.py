# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stops'
        db.create_table(u'busing_stops', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['busing.Bus'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('request', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'busing', ['Stops'])

        # Adding model 'Bus'
        db.create_table(u'busing_bus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shuttle', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'busing', ['Bus'])


    def backwards(self, orm):
        # Deleting model 'Stops'
        db.delete_table(u'busing_stops')

        # Deleting model 'Bus'
        db.delete_table(u'busing_bus')


    models = {
        u'busing.bus': {
            'Meta': {'object_name': 'Bus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shuttle': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'busing.stops': {
            'Meta': {'object_name': 'Stops'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['busing.Bus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'request': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']