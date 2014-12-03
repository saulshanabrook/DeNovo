# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equitytrading', '0006_auto_20141126_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='catogory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 1, 54, 48, 78000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 1, 54, 48, 62000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 1, 54, 48, 62000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
