# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentItApp', '0002_auto_20150727_1601'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product_registration',
            table='product_registration',
        ),
        migrations.AlterModelTable(
            name='productimage',
            table='product_image',
        ),
    ]
