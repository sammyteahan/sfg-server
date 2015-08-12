# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0003_auto_20150810_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
