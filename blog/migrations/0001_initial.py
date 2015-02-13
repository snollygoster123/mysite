# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('ip_address', models.GenericIPAddressField()),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('date', models.DateTimeField(verbose_name='date commented')),
                ('ip_address', models.GenericIPAddressField()),
                ('text', models.TextField()),
                ('blog', models.ForeignKey(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
