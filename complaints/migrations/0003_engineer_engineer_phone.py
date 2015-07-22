# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_auto_20150711_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='engineer_phone',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
