# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import apps.book.models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('isbn_number', models.CharField(unique=True, max_length=100)),
                ('date_recieved', models.DateField(default=datetime.datetime(2015, 6, 9, 13, 23, 50, 249674))),
                ('quantity', models.PositiveIntegerField(default=0, null=True)),
                ('source', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=150, choices=[(b'Science fiction', b'Science fiction'), (b'Satire', b'Satire'), (b'Drama', b'Drama'), (b'Action and Adventure', b'Action and Adventure'), (b'Romance', b'Romance'), (b'Mystery', b'Mystery'), (b'Horror', b'Horror'), (b'Self help', b'Self help'), (b'Guide', b'Guide'), (b'Travel', b'Travel'), (b"Children's", b"Children's"), (b'Religious', b'Religious'), (b'Science', b'Science'), (b'History', b'History'), (b'Math', b'Math'), (b'Anthologies', b'Anthologies'), (b'Poetry', b'Poetry'), (b'Encyclopedias', b'Encyclopedias'), (b'Dictionaries', b'Dictionaries'), (b'Comics', b'Comics'), (b'Art', b'Art'), (b'Cookbooks', b'Cookbooks'), (b'Diaries', b'Diaries'), (b'Journals', b'Journals'), (b'Prayer books', b'Prayer books'), (b'Series', b'Series'), (b'Programming', b'Programming'), (b'Biographies', b'Biographies'), (b'Autobiographies', b'Autobiographies'), (b'Fantasy', b'Fantasy')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookLease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrowed_date', models.DateField(default=datetime.datetime(2015, 6, 9, 13, 23, 50, 250718))),
                ('due_date', models.DateField(default=apps.book.models.get_deadline)),
                ('returned', models.NullBooleanField()),
                ('book', models.ForeignKey(related_name=b'book_leases', to='book.Book')),
                ('borrower', models.ForeignKey(to='libraryuser.Fellow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
