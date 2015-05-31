# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_auto_20150521_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booklease',
            name='return_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(default=datetime.datetime(2015, 5, 31, 20, 54, 0, 880450)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 31, 20, 54, 0, 881858)),
        ),
    ]
