# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equitytrading', '0003_auto_20141126_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 26, 18, 35, 48, 798714, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 26, 18, 35, 48, 797935, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 26, 18, 35, 48, 797493, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
