# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20150507_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklease',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 7, 11, 11, 19, 140326, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booklease',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 7, 11, 11, 30, 404525, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
