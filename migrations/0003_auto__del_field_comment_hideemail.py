# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Comment.hideemail'
        db.delete_column('brewlog_comment', 'hideemail')


    def backwards(self, orm):
        # Adding field 'Comment.hideemail'
        db.add_column('brewlog_comment', 'hideemail',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'brewlog.adjunct': {
            'Meta': {'object_name': 'Adjunct'},
            'addtime': ('django.db.models.fields.IntegerField', [], {}),
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'brewlog.brewday': {
            'Meta': {'object_name': 'BrewDay'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'og': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'targetog': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'}),
            'totalboil': ('django.db.models.fields.IntegerField', [], {}),
            'totalsteep': ('django.db.models.fields.IntegerField', [], {})
        },
        'brewlog.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'brewlog.extract': {
            'Meta': {'object_name': 'Extract'},
            'addtime': ('django.db.models.fields.IntegerField', [], {}),
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'brewlog.fermentationstep': {
            'Meta': {'object_name': 'FermentationStep'},
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'days': ('django.db.models.fields.IntegerField', [], {}),
            'fg': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'targetfg': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'})
        },
        'brewlog.hop': {
            'Meta': {'object_name': 'Hop'},
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'endtime': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'starttime': ('django.db.models.fields.IntegerField', [], {}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'brewlog.otheringredient': {
            'Meta': {'object_name': 'OtherIngredient'},
            'addtime': ('django.db.models.fields.IntegerField', [], {}),
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'endtime': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'starttime': ('django.db.models.fields.IntegerField', [], {})
        },
        'brewlog.steepinggrain': {
            'Meta': {'object_name': 'SteepingGrain'},
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'endtime': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'starttime': ('django.db.models.fields.IntegerField', [], {}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'brewlog.yeast': {
            'Meta': {'object_name': 'Yeast'},
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brewlog.BrewDay']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['brewlog']