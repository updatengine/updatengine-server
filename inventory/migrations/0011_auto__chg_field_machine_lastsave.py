# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'machine.lastsave'
        db.alter_column('inventory_machine', 'lastsave', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'machine.lastsave'
        db.alter_column('inventory_machine', 'lastsave', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default='Null'))

    models = {
        'deploy.package': {
            'Meta': {'object_name': 'package'},
            'command': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'conditions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['deploy.packagecondition']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignoreperiod': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'packagesum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.CharField', [], {'default': "'no'", 'max_length': '3'})
        },
        'deploy.packagecondition': {
            'Meta': {'object_name': 'packagecondition'},
            'depends': ('django.db.models.fields.CharField', [], {'default': "'installed'", 'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'softwarename': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'softwareversion': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'deploy.packageprofile': {
            'Meta': {'object_name': 'packageprofile'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['deploy.package']", 'null': 'True', 'blank': 'True'})
        },
        'deploy.timeprofile': {
            'Meta': {'object_name': 'timeprofile'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'inventory.entity': {
            'Meta': {'object_name': 'entity'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['inventory.entity']"})
        },
        'inventory.machine': {
            'Meta': {'object_name': 'machine'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.entity']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastsave': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'manualy_created': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'netsum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'ossum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'packageprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['deploy.packageprofile']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['deploy.package']", 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'softsum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'timeprofile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['deploy.timeprofile']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'typemachine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.typemachine']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'inventory.net': {
            'Meta': {'object_name': 'net'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.machine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'manualy_created': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '3'}),
            'mask': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'inventory.osdistribution': {
            'Meta': {'object_name': 'osdistribution'},
            'arch': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.machine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manualy_created': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'systemdrive': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'inventory.software': {
            'Meta': {'object_name': 'software'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.machine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manualy_created': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uninstall': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'undefined'", 'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'inventory.typemachine': {
            'Meta': {'object_name': 'typemachine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['inventory']