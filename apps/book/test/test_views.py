from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from apps.book.views import *
from apps.book.models import Book, BookLease
from apps.book.test.factories import BookFactory


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
