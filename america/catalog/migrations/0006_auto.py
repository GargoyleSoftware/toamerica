# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field manager_profiles on 'RegionalCenter'
        db.delete_table('catalog_regionalcenter_manager_profiles')


    def backwards(self, orm):
        # Adding M2M table for field manager_profiles on 'RegionalCenter'
        db.create_table('catalog_regionalcenter_manager_profiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('regionalcenter', models.ForeignKey(orm['catalog.regionalcenter'], null=False)),
            ('manager', models.ForeignKey(orm['catalog.manager'], null=False))
        ))
        db.create_unique('catalog_regionalcenter_manager_profiles', ['regionalcenter_id', 'manager_id'])


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
            'money_raised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'money_to_raise': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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