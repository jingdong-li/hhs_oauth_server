# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-02 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20161102_1911'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRegisterInvite',
            new_name='UserRegisterInvitation',
        ),
    ]