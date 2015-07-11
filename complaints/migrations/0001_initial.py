# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lock_date', models.DateTimeField(verbose_name=b'date locked')),
                ('client_name', models.CharField(max_length=200)),
                ('complaint_details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_name', models.CharField(max_length=150)),
                ('complaint', models.ForeignKey(to='complaints.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='Engineers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engineer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='assigned_to',
            field=models.ForeignKey(to='complaints.Engineers'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='location',
            field=models.ForeignKey(to='complaints.Location'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.ForeignKey(to='complaints.Status'),
        ),
    ]
