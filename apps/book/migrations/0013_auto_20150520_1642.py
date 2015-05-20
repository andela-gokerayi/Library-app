# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import apps.book.models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20150508_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 16, 42, 37, 776713)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 16, 42, 37, 777684)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='due_date',
            field=models.DateField(default=apps.book.models.get_deadline),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 16, 42, 37, 777719)),
        ),
    ]
