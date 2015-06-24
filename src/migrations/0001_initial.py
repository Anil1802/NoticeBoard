# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('event_name', models.CharField(max_length=75)),
                ('event_decription', models.CharField(max_length=1500)),
                ('event_date', models.DateField()),
                ('event_timings', models.TimeField()),
                ('event_venue', models.CharField(max_length=75)),
                ('event_fees', models.IntegerField(default=0)),
                ('event_seats', models.IntegerField(default=30)),
                ('event_organizer_details', models.CharField(max_length=200)),
            ],
        ),
    ]
