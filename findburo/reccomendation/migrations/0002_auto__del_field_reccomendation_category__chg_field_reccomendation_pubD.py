# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reccomendation.category'
        db.delete_column('reccomendation_reccomendation', 'category_id')

        # Adding M2M table for field category on 'Reccomendation'
        db.create_table('reccomendation_reccomendation_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reccomendation', models.ForeignKey(orm['reccomendation.reccomendation'], null=False)),
            ('category', models.ForeignKey(orm['reccomendation.category'], null=False))
        ))
        db.create_unique('reccomendation_reccomendation_category', ['reccomendation_id', 'category_id'])


        # Changing field 'Reccomendation.pubDate'
        db.alter_column('reccomendation_reccomendation', 'pubDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Reccomendation.category'
        raise RuntimeError("Cannot reverse this migration. 'Reccomendation.category' and its values cannot be restored.")
        # Removing M2M table for field category on 'Reccomendation'
        db.delete_table('reccomendation_reccomendation_category')


        # Changing field 'Reccomendation.pubDate'
        db.alter_column('reccomendation_reccomendation', 'pubDate', self.gf('django.db.models.fields.DateTimeField')())

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
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reccomendation.Category']", 'symmetrical': 'False'}),
            'google': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pubDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['reccomendation']