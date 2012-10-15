# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ManagerProfile'
        db.delete_table('catalog_managerprofile')

        # Adding model 'Manager'
        db.create_table('catalog_manager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('catalog', ['Manager'])


        # Changing field 'SocialProfile.manager'
        db.alter_column('catalog_socialprofile', 'manager_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Manager']))

    def backwards(self, orm):
        # Adding model 'ManagerProfile'
        db.create_table('catalog_managerprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('catalog', ['ManagerProfile'])

        # Deleting model 'Manager'
        db.delete_table('catalog_manager')


        # Changing field 'SocialProfile.manager'
        db.alter_column('catalog_socialprofile', 'manager_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ManagerProfile']))

    models = {
        'catalog.businesstobuy': {
            'Meta': {'object_name': 'BusinessToBuy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'catalog.manager': {
            'Meta': {'object_name': 'Manager'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'catalog.regionalcenter': {
            'Meta': {'object_name': 'RegionalCenter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_profiles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['catalog.Manager']", 'null': 'True', 'blank': 'True'}),
            'money_raised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'money_to_raise': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'catalog.serviceprovider': {
            'Meta': {'object_name': 'ServiceProvider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'catalog.socialprofile': {
            'Meta': {'object_name': 'SocialProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Manager']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']