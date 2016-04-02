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

        # Deleting field 'Bus.kind'
        db.delete_column(u'busing_bus', 'kind')

        # Deleting field 'Bus.request'
        db.delete_column(u'busing_bus', 'request')

        # Deleting field 'Bus.location'
        db.delete_column(u'busing_bus', 'location')

        # Deleting field 'Bus.time'
        db.delete_column(u'busing_bus', 'time')


    def backwards(self, orm):
        # Deleting model 'Stops'
        db.delete_table(u'busing_stops')

        # Adding field 'Bus.kind'
        db.add_column(u'busing_bus', 'kind',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Bus.request'
        db.add_column(u'busing_bus', 'request',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Bus.location'
        db.add_column(u'busing_bus', 'location',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Bus.time'
        db.add_column(u'busing_bus', 'time',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


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