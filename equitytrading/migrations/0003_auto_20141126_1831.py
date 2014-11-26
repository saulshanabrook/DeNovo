# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equitytrading', '0002_auto_20141126_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 26, 18, 31, 5, 153722, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='startup',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 26, 18, 31, 5, 153063, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 26, 18, 31, 5, 152619, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
