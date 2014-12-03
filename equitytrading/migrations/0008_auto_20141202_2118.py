# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equitytrading', '0007_auto_20141202_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 2, 18, 17, 89000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 2, 18, 17, 89000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(max_length=1, choices=[(b'S', b'Startup'), (b'B', b'Business')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 2, 18, 17, 89000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
