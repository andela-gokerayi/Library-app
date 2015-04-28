# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20150424_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(),
        ),
    ]
