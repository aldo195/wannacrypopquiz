# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20170821_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='has_auth',
            field=models.CharField(blank=True, choices=[('1', 'My report includes successful scanner authentication.'), ('2', 'My report does NOT have successful scanner authentication.')], default='1', max_length=500),
        ),
        migrations.AddField(
            model_name='drill',
            name='has_eternalblue',
            field=models.CharField(blank=True, choices=[('1', 'My report includes one or more cases of Eternal Blue.'), ('2', 'My report does NOT have any Eternal Blue.')], default='1', max_length=500),
        ),
    ]