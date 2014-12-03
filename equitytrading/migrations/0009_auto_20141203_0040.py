# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equitytrading', '0008_auto_20141202_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 40, 42, 616000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to=b'profile_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 40, 42, 616000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='logo',
            field=models.ImageField(upload_to=b'profile_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 5, 40, 42, 616000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
