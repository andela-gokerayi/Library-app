from datetime import date
from mock import patch

from django.utils.http import urlencode
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from apps.book.models import Book, BookLease, BookBorrowRequest
from apps.book.test.factories import BookFactory, BookBorrowRequestFactory, BookLeaseFactory
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


class BookLeaseListViewTest(BaseViewTest):

    def setUp(self):
        super(BookLeaseListViewTest, self).setUp()
        book_lease = BookLeaseFactory()
        second_book = BookFactory(title='Quantum Mechanics')
        second_book_lease  = BookLeaseFactory(book=second_book, due_date=date(2015, 5, 27))
        third_book = BookFactory(title='Solid State')
        third_book_lease  = BookLeaseFactory(book=third_book, due_date=date(2015, 5, 28))
        fourth_book = BookFactory(title='Digital Electronics')
        fourth_book_lease  = BookLeaseFactory(book=fourth_book, due_date=date(2015, 5, 29))

    def test_get_request_returns_list_of_book_lease(self):

        response = self.client.get(reverse('booklease-list'))

        book_leases = response.context['book_lease_list']
        self.assertEquals(4, book_leases.count())
        self.assertEquals(book_leases[0].book.title, 'String Theory')
        self.assertEquals(book_leases[3].book.title, 'Digital Electronics')

    def test_post_request_when_a_request_all_leases_is_made(self):

        response = self.client.post(reverse('booklease-list'), {'filter': 1})

        book_leases = response.context['book_lease_list']
        self.assertEquals(4, book_leases.count())
        self.assertEquals(book_leases[0].book.title, 'String Theory')
        self.assertEquals(book_leases[3].book.title, 'Digital Electronics')
        self.assertFalse('due' in response.context)

    @patch('apps.book.views.BookLeaseListView.due_date')
    def test_post_request_when_a_request_for_due_books_is_made(self, mock_due_date):
        mock_due_date.return_value = date(2015, 5, 26)

        response = self.client.post(reverse('booklease-list'), {'filter': 2})

        book_leases = response.context['book_lease_list']
        self.assertEquals(2, book_leases.count())
        self.assertEquals(book_leases[0].book.title, 'Quantum Mechanics')
        self.assertEquals(book_leases[1].book.title, 'Solid State')
        self.assertFalse('due' in response.context)

    @patch('apps.book.views.BookLeaseListView.due_date')
    def test_post_request_when_a_request_for_about_to_be_due_books_is_made(self, mock_due_date):
        mock_due_date.return_value = date(2015, 5, 27)

        response = self.client.post(reverse('booklease-list'), {'filter': 3})

        book_leases = response.context['book_lease_list']
        self.assertEquals(2, book_leases.count())
        self.assertEquals(book_leases[0].book.title, 'String Theory')
        self.assertEquals(book_leases[1].book.title, 'Quantum Mechanics')
        self.assertTrue('due' in response.context)

    def test_post_request_when_an_invalid_request_is_made(self):

        response = self.client.post(reverse('booklease-list'), {'filter': 10})

        book_leases = response.context['book_lease_list']
        self.assertEquals(4, book_leases.count())
        self.assertEquals(book_leases[0].book.title, 'String Theory')
        self.assertEquals(book_leases[3].book.title, 'Digital Electronics')
        self.assertFalse('due' in response.context)

