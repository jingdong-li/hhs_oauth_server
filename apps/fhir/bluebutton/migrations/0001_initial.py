# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-13 12:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('server', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crosswalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fhir_id', models.CharField(blank=True, max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FhirServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Friendly Server Name')),
                ('fhir_url', models.URLField(verbose_name='Full URL to FHIR API with terminating /')),
                ('shard_by', models.CharField(default='Patient', max_length=80, verbose_name='Key Resource type')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceTypeControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('override_url_id', models.BooleanField(help_text='Does this resource need to mask the id in the url?')),
                ('override_search', models.BooleanField(help_text="Do search parameters need to be filtered to avoid revealing other people's data?")),
                ('search_block', models.TextField(blank=True, default='', help_text='list of values that need to be removed from search parameters. eg. Patient', max_length=5120)),
                ('search_add', models.TextField(blank=True, default='', help_text='list of keys that need to be added tosearch parameters to filter informationthat is returned. eg. eg. Patient=%PATIENT%', max_length=200)),
                ('group_allow', models.TextField(blank=True, default='', help_text='groups permitted to access resource.', max_length=100)),
                ('group_exclude', models.TextField(blank=True, default='', help_text='groups blocked from accessing resource.', max_length=100)),
                ('default_url', models.URLField(blank=True, verbose_name='Default FHIR URL with terminating / ')),
                ('resource_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.SupportedResourceType')),
            ],
        ),
        migrations.AddField(
            model_name='crosswalk',
            name='fhir_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bluebutton.FhirServer'),
        ),
        migrations.AddField(
            model_name='crosswalk',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

