# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('availability', models.CharField(max_length=60)),
                ('duration', models.CharField(max_length=60)),
                ('cost', models.TextField()),
                ('currency', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idCategory', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clasification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('category_rel', models.ManyToManyField(to='browser.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nam_ent', models.CharField(max_length=50)),
                ('nam_abr', models.CharField(max_length=10)),
                ('country_rel', models.ForeignKey(to='browser.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nam_mun', models.CharField(max_length=50)),
                ('cve_cab', models.CharField(max_length=4)),
                ('nam_cab', models.CharField(max_length=50)),
                ('entity_rel', models.ForeignKey(to='browser.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=60)),
                ('zip_code', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=60)),
                ('manager', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('page', models.URLField()),
                ('facebook', models.CharField(max_length=60, null=True, blank=True)),
                ('youtube', models.CharField(max_length=60, null=True, blank=True)),
                ('whatsapp', models.CharField(max_length=60, null=True, blank=True)),
                ('instagram', models.CharField(max_length=60, null=True, blank=True)),
                ('twitter', models.CharField(max_length=60, null=True, blank=True)),
                ('tumblr', models.CharField(max_length=60, null=True, blank=True)),
                ('business_phone', models.CharField(max_length=60)),
                ('cel_phone', models.CharField(max_length=60, null=True, blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('activity_rel', models.ManyToManyField(to='browser.Activity')),
                ('city_rel', models.ForeignKey(to='browser.Entity')),
                ('country_rel', models.ForeignKey(to='browser.Country')),
                ('state_province_rel', models.ForeignKey(to='browser.Municipality')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='clasification_rel',
            field=models.ManyToManyField(to='browser.Clasification'),
        ),
    ]
