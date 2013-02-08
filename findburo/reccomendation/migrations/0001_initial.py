# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('reccomendation_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('reccomendation', ['Category'])

        # Adding model 'Reccomendation'
        db.create_table('reccomendation_reccomendation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('appstore', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('google', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('youtube', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reccomendation.Category'])),
            ('pubDate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('reccomendation', ['Reccomendation'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('reccomendation_category')

        # Deleting model 'Reccomendation'
        db.delete_table('reccomendation_reccomendation')


    models = {
        'reccomendation.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reccomendation.reccomendation': {
            'Meta': {'object_name': 'Reccomendation'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'appstore': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reccomendation.Category']"}),
            'google': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['reccomendation']