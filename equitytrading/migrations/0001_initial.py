# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('logo', models.ImageField(upload_to=b'')),
                ('location', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=200)),
                ('type_of_service', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('logo', models.ImageField(upload_to=b'')),
                ('location', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('service_needed', models.CharField(max_length=200)),
                ('service_detail', models.TextField(max_length=3000)),
                ('contact_person', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=80)),
                ('contact_phone_number', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catogory', models.CharField(max_length=15)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='startup',
            name='user_profile',
            field=models.ForeignKey(to='equitytrading.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professional',
            name='user_profile',
            field=models.ForeignKey(to='equitytrading.UserProfile'),
            preserve_default=True,
        ),
    ]
