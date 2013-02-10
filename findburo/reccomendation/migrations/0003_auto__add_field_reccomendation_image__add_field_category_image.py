# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reccomendation.image'
        db.add_column('reccomendation_reccomendation', 'image',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Category.image'
        db.add_column('reccomendation_category', 'image',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reccomendation.image'
        db.delete_column('reccomendation_reccomendation', 'image')

        # Deleting field 'Category.image'
        db.delete_column('reccomendation_category', 'image')


    models = {
        'reccomendation.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reccomendation.reccomendation': {
            'Meta': {'object_name': 'Reccomendation'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'appstore': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reccomendation.Category']", 'symmetrical': 'False'}),
            'google': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['reccomendation']