# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20151210_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTwinDigitalProducts',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.coveragecondition',),
        ),
        migrations.CreateModel(
            name='FreeTwinDigitalProducts',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('offer.percentagediscountbenefit',),
        ),
    ]
