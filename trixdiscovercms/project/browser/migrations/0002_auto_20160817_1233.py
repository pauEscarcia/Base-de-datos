# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.RenameModel(
            old_name='Municipality',
            new_name='City',
        ),
        migrations.RenameModel(
            old_name='Clasification',
            new_name='Classification',
        ),
        migrations.RenameModel(
            old_name='Entity',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='clasification_rel',
            new_name='classification_rel',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='nam_mun',
            new_name='nam_city',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='clave',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='nam_ent',
            new_name='nam_sta',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='tumblr',
        ),
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='status',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='youtube',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='images_rel',
            field=models.ManyToManyField(to='browser.Images'),
        ),
    ]
