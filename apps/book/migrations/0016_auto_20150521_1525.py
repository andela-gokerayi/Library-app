# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_auto_20150520_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(default=datetime.datetime(2015, 5, 21, 15, 25, 2, 67992)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 21, 15, 25, 2, 69152)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 21, 15, 25, 2, 69194)),
        ),
    ]
