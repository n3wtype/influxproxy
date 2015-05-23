# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('influx_database', models.CharField(max_length=64)),
                ('default_prefix', models.CharField(max_length=32, default='host')),
            ],
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('prefix', models.CharField(max_length=32, blank=True)),
                ('client', models.ForeignKey(to='influxproxy_base.Client')),
            ],
        ),
    ]
