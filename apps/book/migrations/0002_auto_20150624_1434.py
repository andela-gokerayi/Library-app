# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
