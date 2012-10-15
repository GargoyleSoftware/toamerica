# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ManagerProfile'
        db.create_table('catalog_managerprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('catalog', ['ManagerProfile'])

        # Adding model 'SocialProfile'
        db.create_table('catalog_socialprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ManagerProfile'])),
        ))
        db.send_create_signal('catalog', ['SocialProfile'])

        # Adding model 'RegionalCenter'
        db.create_table('catalog_regionalcenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('money_to_raise', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('money_raised', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('catalog', ['RegionalCenter'])

        # Adding M2M table for field manager_profiles on 'RegionalCenter'
        db.create_table('catalog_regionalcenter_manager_profiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('regionalcenter', models.ForeignKey(orm['catalog.regionalcenter'], null=False)),
            ('managerprofile', models.ForeignKey(orm['catalog.managerprofile'], null=False))
        ))
        db.create_unique('catalog_regionalcenter_manager_profiles', ['regionalcenter_id', 'managerprofile_id'])

        # Adding model 'BusinessToBuy'
        db.create_table('catalog_businesstobuy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('catalog', ['BusinessToBuy'])

        # Adding model 'ServiceProvider'
        db.create_table('catalog_serviceprovider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('catalog', ['ServiceProvider'])


    def backwards(self, orm):
        # Deleting model 'ManagerProfile'
        db.delete_table('catalog_managerprofile')

        # Deleting model 'SocialProfile'
        db.delete_table('catalog_socialprofile')

        # Deleting model 'RegionalCenter'
        db.delete_table('catalog_regionalcenter')

        # Removing M2M table for field manager_profiles on 'RegionalCenter'
        db.delete_table('catalog_regionalcenter_manager_profiles')

        # Deleting model 'BusinessToBuy'
        db.delete_table('catalog_businesstobuy')

        # Deleting model 'ServiceProvider'
        db.delete_table('catalog_serviceprovider')


    models = {
        'catalog.businesstobuy': {
            'Meta': {'object_name': 'BusinessToBuy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'catalog.managerprofile': {
            'Meta': {'object_name': 'ManagerProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'catalog.regionalcenter': {
            'Meta': {'object_name': 'RegionalCenter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_profiles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['catalog.ManagerProfile']", 'null': 'True', 'blank': 'True'}),
            'money_raised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'money_to_raise': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'catalog.serviceprovider': {
            'Meta': {'object_name': 'ServiceProvider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'catalog.socialprofile': {
            'Meta': {'object_name': 'SocialProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.ManagerProfile']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']