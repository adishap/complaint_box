# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_engineer_engineer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
