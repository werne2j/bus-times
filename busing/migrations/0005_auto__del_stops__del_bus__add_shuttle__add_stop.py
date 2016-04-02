# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Stops'
        db.delete_table(u'busing_stops')

        # Deleting model 'Bus'
        db.delete_table(u'busing_bus')

        # Adding model 'Shuttle'
        db.create_table(u'busing_shuttle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bus', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'busing', ['Shuttle'])

        # Adding model 'Stop'
        db.create_table(u'busing_stop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shuttle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['busing.Shuttle'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('request', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'busing', ['Stop'])


    def backwards(self, orm):
        # Adding model 'Stops'
        db.create_table(u'busing_stops', (
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['busing.Bus'])),
            ('request', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'busing', ['Stops'])

        # Adding model 'Bus'
        db.create_table(u'busing_bus', (
            ('shuttle', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'busing', ['Bus'])

        # Deleting model 'Shuttle'
        db.delete_table(u'busing_shuttle')

        # Deleting model 'Stop'
        db.delete_table(u'busing_stop')


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
            'time': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['busing']