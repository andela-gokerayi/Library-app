from django.test import TestCase
from django.db import models
from apps.book.models import Book, BookLease
from apps.libraryuser.models import Fellow
import factory


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book

    title = u'String Theory'


class FellowFactory(factory.DjangoModelFactory):
    class Meta:
        model = Fellow

    first_name = u'John'
    email = u'john@example.com'


class BookLeaseFactory(factory.DjangoModelFactory):
    class Meta:
        model = BookLease

    book = factory.SubFactory(BookFactory)
    borrower = factory.SubFactory(FellowFactory)


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

    def test_get_book_deadline_method_empty_book(self):
        book = BookFactory()

        deadline = book.get_book_deadline()

        self.assertEqual({}, deadline)

    def test_get_book_deadline_method_single_lease(self):
        lease = BookLeaseFactory()

        deadline = lease.book.get_book_deadline()

        self.assertEqual({'john@example.com': 14}, deadline)

    def test_get_book_deadline_method_multiple_leases(self):
        lease1 = BookLeaseFactory()
        borrower = FellowFactory(email='jane@example.com')
        lease2 = BookLeaseFactory(book=lease1.book, borrower=borrower)

        deadline = lease1.book.get_book_deadline()

        self.assertEqual({'john@example.com': 14, 'jane@example.com': 14}, deadline)

    def test_get_num_available_books_with_zero_quantity(self):
        book = BookFactory(quantity=0)

        num_available = book.get_num_available_book()

        self.assertEqual(0, num_available)

    def test_get_num_available_books_with_quantity_greater_than_zero(self):
        book = BookFactory(quantity=3)

        num_available = book.get_num_available_book()

        self.assertEqual(3, num_available)

    def test_get_num_available_books_with_leases(self):
        lease = BookLeaseFactory()

        num_available = lease.book.get_num_available_book()

        self.assertEqual(0, num_available)

     # def get_num_available_book(self):
     #    total_leased = self.book_leases.all().count()
     #    available = self.quantity - total_leased
     #    return available


class BookLeaseModelTest(TestCase):

    """docstring for BookLeaseModelTest"""

    def test_model_fields(self):

        fields = {field.name: field for field in BookLease._meta.fields}

        self.assertTrue(fields.has_key('book'))
        self.assertTrue(fields.has_key('borrower'))
        self.assertTrue(fields.has_key('borrowed_date'))
        self.assertTrue(fields.has_key('due_date'))
        self.assertTrue(fields.has_key('returned'))
