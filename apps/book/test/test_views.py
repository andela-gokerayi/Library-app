from datetime import date
from mock import patch

from django.utils.http import urlencode
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
from apps.book.models import Book, BookLease, BookBorrowRequest
from apps.book.views import BookLeaseListView
from apps.book.test.factories import BookFactory, BookBorrowRequestFactory, BookLeaseFactory
from apps.libraryuser.test.factories import UserFactory, FellowFactory


class BaseViewTest(TestCase):

    def setUp(self):
        password = 'secret'
        self.user = User.objects.create_superuser(username='admin', password=password, email='admin@admin.com')
        self.client = Client()
        logged_in = self.client.login(username=self.user.username, password=password)
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

    def test_due_date_function_returns_a_datetime(self):
        book_lease = BookLeaseListView()

        due_date = book_lease.due_date()

        self.assertEquals(date, type(due_date))


class BookLeaseDetailViewTest(BaseViewTest):

    def test_get_request_for_a_lease_detail_with_valid_id(self):
        book_lease = BookLeaseFactory()

        response = self.client.get(reverse('booklease-detail', args=[book_lease.book.id]))
       
        self.assertTrue('object' in response.context)
        self.assertEquals(response.context['object'].book.title, 'String Theory')

    def test_request_for_a_lease_detail_with_invalid_id(self):

        response = self.client.get(reverse('booklease-detail', args=[999]))
       
        self.assertTrue('object' not in response.context)


class TestGetBookView(BaseViewTest):

    def test_get_request_for_adding_a_new_book(self):
        response = self.client.get(reverse('add-book'))

        self.assertTrue('form' in response.context) 

    def test_post_request_for_adding_a_new_book_when_the_data_is_valid(self):

        data = {
            'title': 'Biology',
            'author': 'Jess',
            'category': 'Science',
            'quantity': '3',
            'source': 'Arinde Eniola',
            'isbn_number': '1234'
        }
        response = self.client.post(reverse('add-book'), data)

        self.assertContains(response, 'Biology Has Been Successfully Added')
        books = Book.objects.filter(title='Biology')
        self.assertEquals(books.count(), 1)

    def test_post_request_for_adding_a_new_book_when_some_of_the_data_are_invalid(self):

        data = {
            'title': '',
            'author': 'Jess',
            'category': 'Science',
            'quantity': 'sdsd',
            'source': 'Arinde Eniola',
            'isbn_number': '1234'
        }
        response = self.client.post(reverse('add-book'), data)

        self.assertContains(response, 'This field is required.')
        self.assertContains(response, 'Enter a whole number.')
        books = Book.objects.all()
        self.assertEquals(books.count(), 0)


class BorrowBookViewTest(BaseViewTest):

    def setUp(self):
        super(BorrowBookViewTest, self).setUp()
        self.book = BookFactory()

    def test_get_request_for_borrowing_a_book_to_fellow(self):
        response = self.client.get(reverse('borrow-book', args=[self.book.id]))

        self.assertTrue('form' in response.context)
        self.assertContains(response, 'String Theory')

    def test_post_request_for_borrowing_a_book_when_the_data_is_valid(self):
        fellow = FellowFactory()
        data = {
            'book': self.book.id,
            'borrower': fellow.id,
            'due_date': date(2015, 7, 3)
        }

        response = self.client.post(reverse('borrow-book', args=[self.book.id]), data)

        self.assertEquals(response.status_code, 302)
        self.assertEquals('http://testserver/home/', response['Location'])
        leases = BookLease.objects.filter(book=self.book)
        self.assertEquals(leases.count(), 1)

    def test_post_request_for_borrowing_a_book_when_the_data_is_not_valid(self):
        fellow = FellowFactory()
        data = {
            'book': self.book.id,
            'borrower': fellow.id
        }

        response = self.client.post(reverse('borrow-book', args=[self.book.id]), data)

        self.assertContains(response, 'This field is required.')
        leases = BookLease.objects.all()
        self.assertEquals(leases.count(), 0)


class LendBookViewTest(BaseViewTest):

    @patch('django.core.mail.send_mail')
    def test_user_is_redirected_if_request_is_successful(self, mock_send_mail):

        password = 'secret'
        self.user = User.objects.create_user(username='eniola', password=password, email='eniola@admin.com')
        logged_in = self.client.login(username=self.user.username, password=password)
        self.assertTrue(logged_in)

        book = BookFactory()

        response = self.client.get(reverse('lend-book', args=[book.id]))

        self.assertEquals(302, response.status_code)
        self.assertEquals('http://testserver/home/', response['Location'])

        new_request = BookBorrowRequest.objects.get(book_name=book)
        self.assertEquals(new_request.borrower, self.user)

        msg = 'A request is been made by %s to borrow the book "%s" ' %(self.user.username, book.title)

        mock_send_mail.assert_called_once_with("Book Lending request", msg, 'andela.library@andela.co',
              ['gbolahan.okerayi@andela.co', 'eniola.arinde@andela.co'])


class BookDeleteViewTest(BaseViewTest):

    def test_redirects_to_home_with_successfull_book_deletion(self):
        book = BookFactory()

        response = self.client.get(reverse('book_delete', args=[book.id]))

        self.assertEquals(302, response.status_code)
        self.assertEquals('http://testserver/home/', response['Location'])

        check_book = Book.objects.filter(id=book.id)
        self.assertEquals(0, check_book.count())

    def test_returns_a_404_if_book_does_not_exist(self):

        response = self.client.get(reverse('book_delete', args=[999]))

        self.assertEquals(404, response.status_code)      


class EditBookViewTest(BaseViewTest):

    def test_get_request_returns_a_template_to_edit_a_book(self):
        book = BookFactory()

        response = self.client.get(reverse('edit-book', args=[book.id]))

        self.assertContains(response, '<label for="id_title">Book Title: </label>')
        self.assertTrue('book' in response.context)

    def test_book_is_edited_when_a_post_request_is_made_with_valid_data(self):
        book = BookFactory()

        data = {
            'title': 'Biology',
            'author': 'Jess',
            'category': 'Science',
            'quantity': '3',
            'source': 'Arinde Eniola',
            'isbn_number': '1234'
        }

        response = self.client.post(reverse('edit-book', args=[book.id]), data)

        self.assertEquals(200, response.status_code)
        self.assertContains(response, '%s Has Been Successfully Edited' % data['title']) 

        updated_book = Book.objects.get(id=book.id)
        self.assertEquals('Jess', updated_book.author) 

    def test_book_is_edited_when_a_post_request_is_made_with_invalid_data(self):
        book = BookFactory()

        data = {
            'title': '',
            'author': 'Jess',
            'category': 'Science',
            'quantity': 'eni',
            'source': 'Arinde Eniola',
            'isbn_number': '1234'
        }

        response = self.client.post(reverse('edit-book', args=[book.id]), data)

        self.assertEquals(200, response.status_code)
        self.assertContains(response, 'This field is required.' ) 
        self.assertContains(response, 'Enter a whole number.' )
       
        updated_book = Book.objects.get(id=book.id)
        self.assertEquals(updated_book.title, 'String Theory') 
