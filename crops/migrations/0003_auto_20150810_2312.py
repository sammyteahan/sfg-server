# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0002_auto_20150809_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='tier',
            field=models.CharField(default=b'1', max_length=255, choices=[(b'1', b'Tier 1'), (b'2', b'Tier 2'), (b'3', b'Tier 3')]),
        ),
    ]
