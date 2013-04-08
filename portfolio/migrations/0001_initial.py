# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('portfolio_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('overview_image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('completion_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('project_type', self.gf('django.db.models.fields.IntegerField')()),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('portfolio', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('portfolio_project')


    models = {
        'portfolio.project': {
            'Meta': {'ordering': "['-completion_date']", 'object_name': 'Project'},
            'completion_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overview_image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'project_type': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['portfolio']