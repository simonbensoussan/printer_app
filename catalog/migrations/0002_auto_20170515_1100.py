# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='remise',
            unique_together=set([('fournisseur', 'produit')]),
        ),
    ]
