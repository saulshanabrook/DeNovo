# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equitytrading', '0009_auto_20141203_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 55, 14, 74000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 55, 14, 74000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 55, 14, 74000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
