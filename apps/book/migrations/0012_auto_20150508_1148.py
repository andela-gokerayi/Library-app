# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20150507_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
