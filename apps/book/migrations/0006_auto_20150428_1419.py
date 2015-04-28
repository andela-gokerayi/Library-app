# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20150428_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 14, 19, 10, 46111, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
