# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-01 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='file',
            field=models.FileField(help_text='.html', upload_to='media/templates/', verbose_name='\u041c\u0430\u043a\u0435\u0442 (.html)'),
        ),
    ]
