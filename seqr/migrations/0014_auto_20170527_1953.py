# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seqr', '0013_auto_20170526_0157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='case_review_requested_info',
            new_name='case_review_discussion',
        ),
    ]
