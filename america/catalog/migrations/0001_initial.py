# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manager'
        db.create_table(u'catalog_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'catalog', ['Manager'])

        # Adding model 'SocialProfile'
        db.create_table(u'catalog_socialprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Manager'])),
        ))
        db.send_create_signal(u'catalog', ['SocialProfile'])

        # Adding model 'RegionalCenter'
        db.create_table(u'catalog_regionalcenter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('money_to_raise', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('money_raised', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['RegionalCenter'])

        # Adding model 'BusinessToBuy'
        db.create_table(u'catalog_businesstobuy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'catalog', ['BusinessToBuy'])

        # Adding model 'ServiceProvider'
        db.create_table(u'catalog_serviceprovider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'catalog', ['ServiceProvider'])


    def backwards(self, orm):
        # Deleting model 'Manager'
        db.delete_table(u'catalog_manager')

        # Deleting model 'SocialProfile'
        db.delete_table(u'catalog_socialprofile')

        # Deleting model 'RegionalCenter'
        db.delete_table(u'catalog_regionalcenter')

        # Deleting model 'BusinessToBuy'
        db.delete_table(u'catalog_businesstobuy')

        # Deleting model 'ServiceProvider'
        db.delete_table(u'catalog_serviceprovider')


    models = {
        u'catalog.businesstobuy': {
            'Meta': {'object_name': 'BusinessToBuy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'catalog.manager': {
            'Meta': {'object_name': 'Manager'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'catalog.regionalcenter': {
            'Meta': {'object_name': 'RegionalCenter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money_raised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'money_to_raise': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'catalog.serviceprovider': {
            'Meta': {'object_name': 'ServiceProvider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalog.socialprofile': {
            'Meta': {'object_name': 'SocialProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Manager']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']