# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20150428_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]