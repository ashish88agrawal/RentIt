# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('pc_id', models.AutoField(serialize=False, primary_key=True)),
                ('pc_name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='Product_registration',
            fields=[
                ('uid', models.IntegerField()),
                ('product_id', models.AutoField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=30, null=True)),
                ('pc_id', models.IntegerField(null=True)),
                ('product_title', models.CharField(max_length=100, null=True)),
                ('product_description', models.CharField(max_length=500, null=True)),
                ('rental_condition', models.CharField(max_length=500, null=True)),
                ('available_from', models.DateField(max_length=6, null=True)),
                ('available_till', models.DateField(max_length=6, null=True)),
            ],
            options={
                'db_table': 'product_registration',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField()),
                ('docfile', models.FileField(upload_to=b'', blank=True)),
            ],
            options={
                'db_table': 'product_image',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('umail', models.EmailField(unique=True, max_length=30)),
                ('upass', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=50)),
                ('umobile', models.CharField(max_length=12, null=True)),
                ('ucity', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'users_registration',
            },
        ),
    ]
