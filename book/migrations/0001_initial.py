# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('isbn_number', models.CharField(max_length=100)),
                ('date_recieved', models.DateField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=0, null=True)),
                ('source', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(default=0, null=True)),
                ('available', models.PositiveIntegerField(default=0, null=True)),
                ('borrowed', models.PositiveIntegerField(default=0, null=True)),
                ('author', models.ForeignKey(related_name='author_status', to='book.Book')),
                ('category', models.ForeignKey(related_name='category_status', to='book.Book')),
                ('title', models.ForeignKey(related_name='title_status', to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='LendBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrower', models.CharField(max_length=250)),
                ('borrower_email', models.EmailField(max_length=254)),
                ('borrowed_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('due_date', models.DateField()),
                ('author', models.ForeignKey(to='book.Book')),
                ('isbn_number', models.ForeignKey(related_name='isbn_number_lend', to='book.Book')),
                ('title', models.ForeignKey(related_name='title_lend', to='book.Book')),
            ],
        ),
    ]
