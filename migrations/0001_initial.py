# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BrewDay'
        db.create_table('brewlog_brewday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('totalboil', self.gf('django.db.models.fields.IntegerField')()),
            ('totalsteep', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('targetog', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
            ('og', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
        ))
        db.send_create_signal('brewlog', ['BrewDay'])

        # Adding model 'FermentationStep'
        db.create_table('brewlog_fermentationstep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('days', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('targetfg', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
            ('fg', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
        ))
        db.send_create_signal('brewlog', ['FermentationStep'])

        # Adding model 'Extract'
        db.create_table('brewlog_extract', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('addtime', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brewlog', ['Extract'])

        # Adding model 'SteepingGrain'
        db.create_table('brewlog_steepinggrain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('starttime', self.gf('django.db.models.fields.IntegerField')()),
            ('endtime', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brewlog', ['SteepingGrain'])

        # Adding model 'Hop'
        db.create_table('brewlog_hop', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('starttime', self.gf('django.db.models.fields.IntegerField')()),
            ('endtime', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brewlog', ['Hop'])

        # Adding model 'Adjunct'
        db.create_table('brewlog_adjunct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('addtime', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brewlog', ['Adjunct'])

        # Adding model 'OtherIngredient'
        db.create_table('brewlog_otheringredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('starttime', self.gf('django.db.models.fields.IntegerField')()),
            ('endtime', self.gf('django.db.models.fields.IntegerField')()),
            ('addtime', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brewlog', ['OtherIngredient'])

        # Adding model 'Yeast'
        db.create_table('brewlog_yeast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewlog.BrewDay'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('manufacturer_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('brewlog', ['Yeast'])


    def backwards(self, orm):
        # Deleting model 'BrewDay'
        db.delete_table('brewlog_brewday')

        # Deleting model 'FermentationStep'
        db.delete_table('brewlog_fermentationstep')

        # Deleting model 'Extract'
        db.delete_table('brewlog_extract')

        # Deleting model 'SteepingGrain'
        db.delete_table('brewlog_steepinggrain')

        # Deleting model 'Hop'
        db.delete_table('brewlog_hop')

        # Deleting model 'Adjunct'
        db.delete_table('brewlog_adjunct')

        # Deleting model 'OtherIngredient'
        db.delete_table('brewlog_otheringredient')

        # Deleting model 'Yeast'
        db.delete_table('brewlog_yeast')


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