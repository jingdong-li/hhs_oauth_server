# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bluebutton', '0007_crosswalk_blue_button'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crosswalk',
            old_name='blue_button',
            new_name='bb_text',
        ),
    ]