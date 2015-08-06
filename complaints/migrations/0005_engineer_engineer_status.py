# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0004_engineer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='engineer_status',
            field=models.ForeignKey(default=1, to='complaints.Engineer_status'),
            preserve_default=False,
        ),
    ]
