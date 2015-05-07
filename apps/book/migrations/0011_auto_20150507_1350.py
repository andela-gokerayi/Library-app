# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20150507_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='due_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='return_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
