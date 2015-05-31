# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_auto_20150531_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=150, choices=[(b'Science fiction', b'Science fiction'), (b'Satire', b'Satire'), (b'Drama', b'Drama'), (b'Action and Adventure', b'Action and Adventure'), (b'Romance', b'Romance'), (b'Mystery', b'Mystery'), (b'Horror', b'Horror'), (b'Self help', b'Self help'), (b'Guide', b'Guide'), (b'Travel', b'Travel'), (b"Children's", b"Children's"), (b'Religious', b'Religious'), (b'Science', b'Science'), (b'History', b'History'), (b'Math', b'Math'), (b'Anthologies', b'Anthologies'), (b'Poetry', b'Poetry'), (b'Encyclopedias', b'Encyclopedias'), (b'Dictionaries', b'Dictionaries'), (b'Comics', b'Comics'), (b'Art', b'Art'), (b'Cookbooks', b'Cookbooks'), (b'Diaries', b'Diaries'), (b'Journals', b'Journals'), (b'Prayer books', b'Prayer books'), (b'Series', b'Series'), (b'Programming', b'Programming'), (b'Biographies', b'Biographies'), (b'Autobiographies', b'Autobiographies'), (b'Fantasy', b'Fantasy')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_recieved',
            field=models.DateField(default=datetime.datetime(2015, 5, 31, 21, 52, 10, 264226)),
        ),
        migrations.AlterField(
            model_name='booklease',
            name='borrowed_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 31, 21, 52, 10, 265601)),
        ),
    ]
