# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0004_crop_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
    ]
