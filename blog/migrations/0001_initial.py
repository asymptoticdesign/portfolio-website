# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table('blog_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('overview_image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('post_twitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('twitter_text', self.gf('django.db.models.fields.CharField')(max_length=144, blank=True)),
        ))
        db.send_create_signal('blog', ['Entry'])

        # Adding model 'Link'
        db.create_table('blog_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('via_name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('via_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('overview_image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('post_delicious', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('post_twitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('twitter_text', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
        ))
        db.send_create_signal('blog', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table('blog_entry')

        # Deleting model 'Link'
        db.delete_table('blog_link')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('codename',)", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'blog.entry': {
            'Meta': {'ordering': "['-publish_date']", 'object_name': 'Entry'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overview_image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'post_twitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'twitter_text': ('django.db.models.fields.CharField', [], {'max_length': '144', 'blank': 'True'})
        },
        'blog.link': {
            'Meta': {'ordering': "['-publish_date']", 'object_name': 'Link'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overview_image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'post_delicious': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'post_twitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'twitter_text': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'via_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'via_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']