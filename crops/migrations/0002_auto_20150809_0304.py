# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='category',
            field=models.ForeignKey(related_name='crops', to='crops.Category'),
        ),
    ]
