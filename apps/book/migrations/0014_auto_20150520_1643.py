# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20150520_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 16, 43, 17, 267136)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 16, 43, 17, 267988)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 16, 43, 17, 268016)),
        ),
    ]
