# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_amc_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amc_client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=200)),
                ('renewal_date', models.DateTimeField(verbose_name=b'Renewal date')),
                ('reminder_date', models.DateTimeField(verbose_name=b'Reminder date')),
                ('amc_type', models.ForeignKey(to='complaints.Amc_type')),
            ],
        ),
    ]
