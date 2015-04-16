from django.test import TestCase
from django.db import models
from apps.book.models import Book
from apps.book.models import BookLease

# Create your tests here.
class BookModelTest(TestCase):

    """docstring for BookModelTest"""

    def test_model_fields(self):

        fields = {field.name: field for field in Book._meta.fields}

        self.assertTrue(fields.has_key('title'))
        self.assertTrue(fields.has_key('author'))
        self.assertTrue(fields.has_key('isbn_number'))
        self.assertTrue(fields.has_key('date_recieved'))
        self.assertTrue(fields.has_key('quantity'))
        self.assertTrue(fields.has_key('source'))
        self.assertTrue(fields.has_key('category'))


class BookLeaseModelTest(TestCase):

    """docstring for BookLeaseModelTest"""

    def test_model_fields(self):

        fields = {field.name: field for field in BookLease._meta.fields}

        self.assertTrue(fields.has_key('book'))
        self.assertTrue(fields.has_key('borrower'))
        self.assertTrue(fields.has_key('borrowed_date'))
        self.assertTrue(fields.has_key('return_date'))
        self.assertTrue(fields.has_key('due_date'))
        self.assertTrue(fields.has_key('returned'))