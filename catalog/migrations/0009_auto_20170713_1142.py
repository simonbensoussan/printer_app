# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-13 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20170713_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='your img path', max_length=1000, verbose_name='image du produit'),
        ),
    ]