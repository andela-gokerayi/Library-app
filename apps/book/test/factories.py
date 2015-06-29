import factory
from datetime import date

from django.contrib.auth.models import User
from apps.book.models import Book, BookLease, BookBorrowRequest
from apps.libraryuser.test.factories import FellowFactory, UserFactory


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book

    title = u'String Theory'


class BookLeaseFactory(factory.DjangoModelFactory):
    class Meta:
        model = BookLease

    book = factory.SubFactory(BookFactory)
    borrower = factory.SubFactory(FellowFactory)
    due_date = date(2015, 5, 26)


class BookBorrowRequestFactory(factory.DjangoModelFactory):
    class Meta:
        model = BookBorrowRequest

    book_name = factory.SubFactory(BookFactory)
    borrower = factory.SubFactory(UserFactory)