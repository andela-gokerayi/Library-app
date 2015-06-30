from django.utils.http import urlencode
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from apps.book.views import *
from apps.book.models import Book, BookLease, BookBorrowRequest
from apps.book.test.factories import BookFactory, BookBorrowRequestFactory
from apps.libraryuser.test.factories import UserFactory, FellowFactory


class BaseViewTest(TestCase):

    def setUp(self):
        password = 'secret'
        user = User.objects.create_superuser(username='admin', password=password, email='admin@admin.com')
        self.client = Client()
        logged_in = self.client.login(username=user.username, password=password)
        self.assertTrue(logged_in)


class BookListViewTests(BaseViewTest):

    def test_books_in_the_content_there_is_no_book(self):
        
        response = self.client.get(reverse('book-list'))

        self.assertEquals(list(response.context['object_list']), [])

    def test_books_in_the_content_if_there_is_a_book(self):
        BookFactory()

        response = self.client.get(reverse('book-list'))

        self.assertEquals(response.context['object_list'].count(), 1)


class BookDetailViewTest(BaseViewTest):

    def test_book_information_no_book(self):
        response = self.client.get(reverse('book-detail', args=[999]))

        self.assertEquals(404, response.status_code)

    def test_book_information_with_book(self):
        book = BookFactory()

        response = self.client.get(reverse('book-detail', args=[book.id]))

        self.assertEquals(response.context['object'].title, 'String Theory')


class AdminResponseViewTest(BaseViewTest):

    def test_lend_request_for_book(self):
        book_request = BookBorrowRequestFactory()
        fellow = FellowFactory(email=book_request.borrower.email)

        url = reverse('admin_response')
        query_params = {
            'type':'lend',
            'book': book_request.book_name.id,
            'name': book_request.borrower.username
        }

        response = self.client.get('%s?%s' %(url, urlencode(query_params)))

        self.assertEquals(302, response.status_code)
        url_parts = response['Location'].split('/')
        self.assertEquals('detail', url_parts[3])
        self.assertEquals('%s' % book_request.book_name.id, url_parts[4])

        updated_request = BookBorrowRequest.objects.get(id=book_request.id)
        self.assertEquals(True, updated_request.is_allowed)

    def test_refuse_request_for_a_book(self):
        book_request = BookBorrowRequestFactory()

        query_params = {
            'book': book_request.book_name.id,
            'name': book_request.borrower.username
        }

        url = reverse('admin_response')
        response = self.client.get('%s?%s' %(url, urlencode(query_params)))

        self.assertEquals(302, response.status_code)
        url_parts = response['Location'].split('/')
        self.assertEquals('detail', url_parts[3])
        self.assertEquals('%s' % book_request.book_name.id, url_parts[4])

        updated_requests = BookBorrowRequest.objects.filter(id=book_request.id)
        self.assertEquals(0, updated_requests.count())

