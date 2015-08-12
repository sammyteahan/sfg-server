# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'winter', max_length=255, choices=[(b'summer', b'Summer'), (b'winter', b'Winter'), (b'spring', b'Spring'), (b'fall', b'Fall')])),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('plant_start_date', models.DateField()),
                ('plant_end_date', models.DateField()),
                ('tier', models.CharField(default=b'tier_1', max_length=255, choices=[(b'tier_1', b'Tier 1'), (b'tier_2', b'Tier 2'), (b'tier_3', b'Tier 3')])),
                ('transplant', models.BooleanField(default=None)),
                ('direct_seed', models.BooleanField(default=None)),
                ('category', models.ForeignKey(to='crops.Category')),
            ],
        ),
    ]
