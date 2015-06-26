from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
# from django_dynamic_fixture import G
from django.core.handlers.wsgi import WSGIRequest as HttpRequest
# from selenium import webdriver
# from django.http import HttpRequest
from apps.book.views import *
from apps.book.models import Book, BookLease

class BookListViewTests(TestCase):
    """docstring for BookListViewTests"""
    def test_books_in_the_content(self):
        password = 'secret'
        user = User.objects.create_superuser(username='admin', password=password, email='admin@admin.com')
    
        client = Client()
        logged_in = client.login(username=user.username, password=password)
        self.assertTrue(logged_in)
        
        response = client.get('/home/')

        self.assertEquals(list(response.context['object_list']), [])

        Book.objects.create(title='getting things done',
                            author='david allen', 
                            isbn_number='22434643436',
                            date_recieved='2015-04-16',
                            quantity='3',
                            source='dave',
                            category='professional development'
                            )
        response = client.get('/home/')
        self.assertEquals(response.context['object_list'].count(), 1)
