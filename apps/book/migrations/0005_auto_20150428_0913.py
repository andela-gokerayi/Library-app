# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20150428_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 28, 9, 13, 2, 99636)),
        ),
    ]
