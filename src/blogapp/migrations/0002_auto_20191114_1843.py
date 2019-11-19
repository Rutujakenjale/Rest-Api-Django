# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='article',
            name='name',
        ),
        migrations.AddField(
            model_name='article',
            name='Author',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='Title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
