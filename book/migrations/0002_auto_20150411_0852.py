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
            name='author',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='source',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bookstatus',
            name='author',
            field=models.OneToOneField(related_name='author_status', to_field=b'author', to='book.Book'),
        ),
        migrations.AlterField(
            model_name='bookstatus',
            name='category',
            field=models.OneToOneField(related_name='category_status', to_field=b'category', to='book.Book'),
        ),
        migrations.AlterField(
            model_name='lendbook',
            name='author',
            field=models.OneToOneField(related_name='author_lend', to_field=b'author', to='book.Book'),
        ),
        migrations.AlterField(
            model_name='lendbook',
            name='isbn_number',
            field=models.OneToOneField(related_name='isbn_number_lend', to_field=b'isbn_number', to='book.Book'),
        ),
    ]
