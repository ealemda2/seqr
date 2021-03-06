# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seqr', '0043_auto_20180719_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyAnalysedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(db_index=True, max_length=30, unique=True)),
                ('created_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('last_modified_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seqr.Family')),
            ],
        ),
    ]
