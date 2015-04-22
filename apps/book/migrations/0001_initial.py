# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('date_recieved', models.DateField()),
                ('quantity', models.PositiveIntegerField(default=0, null=True)),
                ('source', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookLease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrowed_date', models.DateField(null=True)),
                ('return_date', models.DateField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('returned', models.NullBooleanField()),
                ('book', models.ForeignKey(related_name='book_leases', to='book.Book')),
                ('borrower', models.ForeignKey(to='libraryuser.Fellow')),
            ],
        ),
    ]
